import os

import numpy as np
from astropy.io import fits

from calcos import average


def create_count_file(file=None):
    """
    creates a temp count file for testing avg_image.

    Parameters
    ----------
    file: str
        the filename string

    Returns
    -------
    filename string
    """
    if file is None:
        file = 'test_count.fits'
    rootname = file[:file.index('_')]
    prim_hdu = fits.PrimaryHDU()
    prim_hdu.header.set('NEXTEND', '3', 'Number of standard extensions')
    prim_hdu.header.set('DATE', '2021-07-26', 'date this file was written (yyyy-mm-dd)')
    prim_hdu.header.set('FILENAME', file, 'name of file')
    prim_hdu.header.set('FILETYPE', 'SCI', 'type of data found in data file')
    prim_hdu.header.set('TELESCOP', 'HST', 'telescope used to acquire data')
    prim_hdu.header.set('EQUINOX', 2000.0, 'equinox of celestial coord. system')
    prim_hdu.header.set('ROOTNAME', rootname, 'rootname of the observation set')
    prim_hdu.header.set('IMAGETYP', 'ACCUM', 'type of exposure identifier')
    prim_hdu.header.set('PRIMESI', 'COS', 'instrument designated as prime')
    prim_hdu.header.set('TARGNAME', '1235867', 'proposer\'s')
    prim_hdu.header.set('RA_TARG', 1.500923600000E+02, 'right ascension of the target (deg) (J2000)')
    prim_hdu.header.set('DEC_TARG', 2.361461111111E+00, 'declination of the target (deg) (J2000)')
    prim_hdu.header.set('PROPOSID', 13313, 'PEP proposal identifier')
    prim_hdu.header.set('LINENUM', '03.001', 'proposal logsheet line number')
    prim_hdu.header.set('PR_INV_L', 'Boquien', 'last name of principal investigator')
    prim_hdu.header.set('PR_INV_F', 'Mederic', 'first name of principal investigator')
    prim_hdu.header.set('PR_INV_M', ' ', 'middle name / initial of principal investigat')
    prim_hdu.header.set('OPT_ELEM', 'MIRRORA', 'optical element in use')
    prim_hdu.header.set('DETECTOR', 'NUV', 'FUV OR NUV')
    prim_hdu.header.set('OBSMODE', 'ACCUM', 'operating mode')
    prim_hdu.header.set('OBSTYPE', 'IMAGING', 'imaging or spectroscopic')
    prim_hdu.header.set('APERTURE', 'PSA', 'aperture name')

    # imageHDU
    imgHDU = fits.ImageHDU()
    imgHDU.header.set('EXTNAME', 'SCI', 'extension version number')
    imgHDU.header.set('EXTVER', 1, 'extension version number')
    imgHDU.header.set('ROOTNAME', rootname, 'rootname of the observation set')
    imgHDU.header.set('EXPNAME', rootname, 'exposure identifier')
    imgHDU.header.set('ASN_MTYP', 'EXP-FP', 'Role of the Member in the Association')
    imgHDU.header.set('WCSAXES', 2, 'number of World Coordinate System axes')
    imgHDU.header.set('CD1_1', 6.12377E-06, 'partial of first axis coordinate w.r.t. x')
    imgHDU.header.set('CD1_2', -3.72298E-06, 'partial of first axis coordinate w.r.t. y')
    imgHDU.header.set('CD2_1', -3.72298E-06, 'partial of second axis coordinate w.r.t. x')
    imgHDU.header.set('CD2_2', 6.12377E-06, 'partial of first axis coordinate w.r.t. y')
    imgHDU.header.set('LTV1', 0.0, 'offset in X to subsection start')
    imgHDU.header.set('LTV2', 0.0, 'offset in Y to subsection start')
    imgHDU.header.set('LTM1_1', 1.0, 'reciprocal of sampling rate in X')
    imgHDU.header.set('LTM2_2', 1.0, 'reciprocal of sampling rate in Y')
    imgHDU.header.set('RA_APER', 1.500923600000E+02, 'RA of reference aperture center')
    imgHDU.header.set('DEC_APER', 2.361461111111E+00, 'Declination of reference aperture center')
    imgHDU.header.set('PA_APER', -3.129775238037E+01, 'Position Angle of reference aperture center (de')
    imgHDU.header.set('DISPAXIS', 0, 'dispersion axis; 1 = axis 1, 2 = axis 2, none')
    imgHDU.header.set('SHIFT1A', 0.0, 'wavecal shift determined spectral strip A(pixel')
    imgHDU.header.set('SHIFT1B', 0.0, 'wavecal shift determined spectral strip B(pixel')
    imgHDU.header.set('SHIFT1C', 0.0, 'wavecal shift determined spectral strip C(pixel')
    imgHDU.header.set('SHIFT2A', 0.0, 'Offset in cross-dispersion direction, A (pixels')
    imgHDU.header.set('SHIFT2B', 0.0, 'Offset in cross-dispersion direction, B (pixels')
    imgHDU.header.set('SHIFT2C', 0.0, 'Offset in cross-dispersion direction, C (pixels')
    imgHDU.header.set('DPIXEL1A', 0.0, 'Average fraction part of pixel coordinate(pixel')
    imgHDU.header.set('DPIXEL1B', 0.0, 'Average fraction part of pixel coordinate(pixel')
    imgHDU.header.set('DPIXEL1C', 0.0, 'Average fraction part of pixel coordinate(pixel')
    imgHDU.header.set('SP_LOC_A', -999.0, 'location of spectral extraction region A')
    imgHDU.header.set('SP_LOC_B', -999.0, 'location of spectral extraction region B')
    imgHDU.header.set('SP_LOC_C', -999.0, 'location of spectral extraction region C')
    imgHDU.header.set('SP_OFF_A', -999.0, 'XD spectrum offset from expected loc (stripe A)')
    imgHDU.header.set('SP_OFF_B', -999.0, 'XD spectrum offset from expected loc (stripe B)')
    imgHDU.header.set('SP_OFF_C', -999.0, 'XD spectrum offset from expected loc (stripe C)')
    imgHDU.header.set('SP_NOM_A', -999.0, 'Expected location of spectrum in XD (stripe A)')
    imgHDU.header.set('SP_NOM_B', -999.0, 'Expected location of spectrum in XD (stripe B)')
    imgHDU.header.set('SP_NOM_C', -999.0, 'Expected location of spectrum in XD (stripe C)')
    imgHDU.header.set('SP_SLP_A', -999.0, 'slope of stripe A spectrum')
    imgHDU.header.set('SP_SLP_B', -999.0, 'slope of stripe B spectrum')
    imgHDU.header.set('SP_SLP_C', -999.0, 'slope of stripe C spectrum')
    imgHDU.header.set('SP_HGT_A', -999.0, 'height (pixels) of stripe A extraction region')
    imgHDU.header.set('SP_HGT_B', -999.0, 'height (pixels) of stripe B extraction region')
    imgHDU.header.set('SP_HGT_C', -999.0, 'height (pixels) of stripe C extraction region')
    imgHDU.header.set('X_OFFSET', 0, 'offset of detector in a calibrated image')
    imgHDU.header.set('B_HGT1_A', -999.0, 'height of spectral background 1 stripe A')
    imgHDU.header.set('B_HGT1_B', -999.0, 'height of spectral background 1 stripe B')
    imgHDU.header.set('B_HGT1_C', -999.0, 'height of spectral background 1 stripe C')
    imgHDU.header.set('B_HGT2_A', -999.0, 'height of spectral background 2 stripe A')
    imgHDU.header.set('B_HGT2_B', -999.0, 'height of spectral background 2 stripe B')
    imgHDU.header.set('B_HGT2_C', -999.0, 'height of spectral background 2 stripe C')
    imgHDU.header.set('B_BKG1_A', -999.0, 'location of spectral background 1 stripe A')
    imgHDU.header.set('B_BKG1_B', -999.0, 'location of spectral background 1 stripe B')
    imgHDU.header.set('B_BKG1_C', -999.0, 'location of spectral background 1 stripe C')
    imgHDU.header.set('B_BKG2_A', -999.0, 'location of spectral background 2 stripe A')
    imgHDU.header.set('B_BKG2_B', -999.0, 'location of spectral background 2 stripe B')
    imgHDU.header.set('B_BKG2_C', -999.0, 'location of spectral background 2 stripe C')
    imgHDU.header.set('ORIENTAT', -31.2978, 'position angle of image y axis (deg. e of n)')
    imgHDU.header.set('SUNANGLE', 125.602852, 'angle between sun and V1 axis')
    imgHDU.header.set('MOONANGL', 55.101593, 'angle between moon and V1 axis')
    imgHDU.header.set('SUN_ALT', 69.923927, 'altitude of the sun above Earth\'s limb')
    imgHDU.header.set('FGSLOCK', 'FINE              ', 'commanded FGS lock (FINE,COARSE,GYROS,UNKNOWN)')
    imgHDU.header.set('GYROMODE', 'T', 'number of gyros scheduled, T=3+OBAD')
    imgHDU.header.set('REFFRAME', 'ICRS    ', 'guide star catalog version')
    imgHDU.header.set('DATE-OBS', '2014-04-15', 'UT date of start of observation (yyyy-mm-dd)')
    imgHDU.header.set('TIME-OBS', '09:20:03', 'UT time of start of observation (hh:mm:ss)')
    imgHDU.header.set('EXPSTART', 5.676238893322E+04, 'exposure start time (Modified Julian Date)')
    imgHDU.header.set('EXPEND', 5.676239032211E+04, 'exposure end time (Modified Julian Date)')
    imgHDU.header.set('EXPTIME', 120.000000, 'exposure duration (seconds)--calculated')
    imgHDU.header.set('EXPFLAG', 'NORMAL       ', 'Exposure interruption indicator')
    imgHDU.header.set('EXPSTRTJ', 2.456762888933E+06, 'start time (JD) of exposure')
    imgHDU.header.set('EXPENDJ', 2.456762890322E+06, 'end time (JD) of exposure')
    imgHDU.header.set('PLANTIME', 120.0, 'Planned exposure time (seconds)')
    imgHDU.header.set('NINTERPT', 0, 'Number of Exposure Interrupts')
    imgHDU.header.set('V_HELIO', -999.0, 'Geocentric to heliocentric velocity')
    imgHDU.header.set('V_LSRSTD', 0.0, 'Heliocentric to standard solar LSR')
    imgHDU.header.set('ORBITPER', 5719.436344, 'Orbital Period used on board for Doppler corr.')
    imgHDU.header.set('DOPPER', 0.0, 'Doppler shift period (seconds)')
    imgHDU.header.set('DOPPMAG', -1.000000, 'Doppler shift magnitude (low-res pixels)')
    imgHDU.header.set('DOPPMAGV', 7.014199, 'Doppler shift magnitude (Km/sec)')
    imgHDU.header.set('DOPPON', 'F', 'Doppler correction flag')
    imgHDU.header.set('DOPPZERO', 56762.336061, 'Commanded time of zero Doppler shift (MJD)')
    imgHDU.header.set('ORBTPERT', -1.0, 'Orbital Period used on board for Doppler corr.')
    imgHDU.header.set('DOPMAGT', -1.0, 'Doppler shift magnitude (low-res pixels)')
    imgHDU.header.set('DOPPONT', 'F', 'Doppler correction flag')
    imgHDU.header.set('DOPZEROT', -1.0, 'Commanded time of zero Doppler shift (MJD)')
    imgHDU.header.set('GLOBRATE', 809.025, 'global count rate')
    imgHDU.header.set('NSUBARRY', 1, 'Number of subarrays (1-8)')
    imgHDU.header.set('CORNER0X', 0, 'subarray axis1 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER1X', 0, 'subarray axis1 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER2X', 0, 'subarray axis1 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER3X', 0, 'subarray axis1 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER4X', 0, 'subarray axis1 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER5X', 0, 'subarray axis1 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER6X', 0, 'subarray axis1 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER7X', 0, 'subarray axis1 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER0Y', 0, 'subarray axis2 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER1Y', 0, 'subarray axis2 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER2Y', 0, 'subarray axis2 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER3Y', 0, 'subarray axis2 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER4Y', 0, 'subarray axis2 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER5Y', 0, 'subarray axis2 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER6Y', 0, 'subarray axis2 corner pt in unbinned dect. pix')
    imgHDU.header.set('CORNER7Y', 0, 'subarray axis2 corner pt in unbinned dect. pix')
    imgHDU.header.set('SIZE0X', 1024, 'subarray 0 axis1 size in unbinned detector pixe')
    imgHDU.header.set('SIZE1X', 0, 'subarray 1 axis1 size in unbinned detector pixe')
    imgHDU.header.set('SIZE2X', 0, 'subarray 2 axis1 size in unbinned detector pixe')
    imgHDU.header.set('SIZE3X', 0, 'subarray 3 axis1 size in unbinned detector pixe')
    imgHDU.header.set('SIZE4X', 0, 'subarray 4 axis1 size in unbinned detector pixe')
    imgHDU.header.set('SIZE5X', 0, 'subarray 5 axis1 size in unbinned detector pixe')
    imgHDU.header.set('SIZE6X', 0, 'subarray 6 axis1 size in unbinned detector pixe')
    imgHDU.header.set('SIZE7X', 0, 'subarray 7 axis1 size in unbinned detector pixe')
    imgHDU.header.set('SIZE0Y', 1024, 'subarray 0 axis2 size in unbinned detector pixe')
    imgHDU.header.set('SIZE1Y', 0, 'subarray 1 axis2 size in unbinned detector pixe')
    imgHDU.header.set('SIZE2Y', 0, 'subarray 2 axis2 size in unbinned detector pixe')
    imgHDU.header.set('SIZE3Y', 0, 'subarray 3 axis2 size in unbinned detector pixe')
    imgHDU.header.set('SIZE4Y', 0, 'subarray 4 axis2 size in unbinned detector pixe')
    imgHDU.header.set('SIZE5Y', 0, 'subarray 5 axis2 size in unbinned detector pixe')
    imgHDU.header.set('SIZE6Y', 0, 'subarray 6 axis2 size in unbinned detector pixe')
    imgHDU.header.set('SIZE7Y', 0, 'subarray 7 axis2 size in unbinned detector pixe')

    imgHDU.header.set('PHOTFLAM', 4.816554456084E-18, 'inverse sensitivity, ergs/s/cm2/Ang per count/s')
    imgHDU.header.set('PHOTFNU ', 8.64540709538E-30, 'inverse sensitivity, ergs/s/cm2/Hz per count/s')
    imgHDU.header.set('PHOTBW  ', 382.88, 'RMS bandwidth of filter plus detector (Ang)')
    imgHDU.header.set('PHOTPLAM', 2319.7, 'Pivot wavelength')
    imgHDU.header.set('PHOTZPT ', -21.10, 'ST magnitude zero point')

    img_errHDU = fits.ImageHDU()
    img_errHDU.header.set('EXTNAME', 'ERR', 'extension name')
    img_errHDU.header.set('EXTVER', 1, 'extension version name')
    img_errHDU.header.set('ROOTNAME', rootname, 'rootname of the observation set')
    img_errHDU.header.set('EXPNAME', rootname, 'exposure identifier')
    img_errHDU.header.set('DATAMIN ', 0.0, 'the minimum value of the data')
    img_errHDU.header.set('DATAMAX ', 0.0, 'the maximum value of the data')
    img_errHDU.header.set('BUNIT   ', 'count /s', 'brightness units')

    dqHDU = fits.ImageHDU()
    dqHDU.header.set('EXTNAME', 'DQ', 'extension name')
    dqHDU.header.set('EXTVER', 1, 'extension version name')
    dqHDU.header.set('ROOTNAME', rootname, 'rootname of the observation set')
    dqHDU.header.set('EXPNAME', rootname, 'exposure identifier')
    dqHDU.header.set('DATAMIN ', 0.0, 'the minimum value of the data')
    dqHDU.header.set('DATAMAX ', 0.0, 'the maximum value of the data')
    dqHDU.header.set('BUNIT   ', 'UNITLESS', 'brightness units')
    sci_data = np.zeros((1024, 1024))
    err_data = np.zeros((1024, 1024))
    dq_data = np.zeros((1024, 1024), dtype='int16')
    for i in range(1024):
        for j in range(1024):
            sci_data[i][j] = 0.00000234
            err_data[i][j] = 0.01534185
            dq_data[i][j] = 8
    imgHDU.data = np.array(sci_data)
    img_errHDU.data = np.array(err_data)
    dqHDU.data = np.array(dq_data)
    hdu_list = fits.HDUList([prim_hdu, imgHDU, img_errHDU, dqHDU])

    if os.path.exists(file):
        os.remove(file)
    hdu_list.writeto(file)
    return file


def test_avg_image():
    """
    tests avg_image() in average.py
    explanation of the test
    - create temporary count files to be used as inputs
    - expected values in the output file are the average of the input values
    - loop though the values to check if the math holds.
    Returns
    -------
    pass if expected == actual fail otherwise.
    """
    # Setup
    infile = ["test_count1.fits", "test_count2.fits"]
    outfile = "test_output.fits"
    if os.path.exists(outfile):
        os.remove(outfile)  # avoid file exists error
    create_count_file(infile[0])
    create_count_file(infile[1])
    inhdr1, inhdr2 = fits.open(infile[0]), fits.open(infile[1])
    # Test
    average.avgImage(infile, outfile)
    out_hdr = fits.open(outfile)

    # Verify
    assert os.path.exists(outfile)
    for (i, j, k) in zip(inhdr1[1].header, inhdr2[1].header, out_hdr[1].header):
        assert i == j == k
    np.testing.assert_array_equal((inhdr1[1].data + inhdr1[1].data) / 2, out_hdr[1].data)
