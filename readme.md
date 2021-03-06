This is an altered version of the Hipparcos catalog inteneded to be easier to use.  The original catalog has RA/DEC coordinates
for the equinox of 1991.25.  Here I have converted the coordinates to J2000 using the NOVAS function "transform_hip".  I have
also removed many fields which are of little use to amateurs.  There are several versions available here, which contain
stars down to different magnitude levels.  For example Hipparcos_6.js contains all stars with magnitude less than 6.  Magnitude
6.5 gets special recognition since it is considered to be the limiting magnitude of human vision.  Though sky conditions
will affect the actual limit.

|Size (bytes)|Name|Stars|
|----|----|-----|
|       41k, 8k |hipparcos_3.js    |   173|
|      125k, 23k |hipparcos_4.js    |   516|
|      390k, 70k |hipparcos_5.js    |  1607|
|      1.2M, 217k |hipparcos_6.js    |  4993|
|      2.1M, 381k |hipparcos_6.5.js  |  8786|
|      3.7M, 666k |hipparcos_7.js    | 15398|
|      9.9M, 1.7M |hipparcos_8.js    | 41058|
|       20M, 3.5M |hipparcos_9.js    | 82985|
|       26M, 4.6M |hipparcos_10.js   |107754|
|       28M, 4.9M |hipparcos_11.js   |115240|
|       28M, 5.1M |hipparcos_12.js   |117454|
|       28M, 5.1M |hipparcos_full.js |117957|


The hip2j2000.py script is what was used to do the conversion.  You must "pip install novas" before running it.

The concise versions retain the following fields:
0    1         9- 14  I6    ---     HIP       Identifier (HIP number)                   (H1)
1    5        42- 46  F5.2  mag     Vmag      ? Magnitude in Johnson V                  (H5)
2    8        52- 63  F12.8 deg     RAdeg    *? alpha, degrees (ICRS, Epoch=J1991.25)   (H8)
3    9        65- 76  F12.8 deg     DEdeg    *? delta, degrees (ICRS, Epoch=J1991.25)   (H9)
4    37      246-251  F6.3  mag     B-V       ? Johnson B-V colour                     (H37)

Below are the fields retained.  You may wish to edit the script to produce files with different fields.:
 0    1         9- 14  I6    ---     HIP       Identifier (HIP number)                   (H1)
 1    2            16  A1    ---     Proxy    *[HT] Proximity flag                       (H2)
 2    5        42- 46  F5.2  mag     Vmag      ? Magnitude in Johnson V                  (H5)
 3    6            48  I1    ---     VarFlag  *[1,3]? Coarse variability flag            (H6)
 4    8        52- 63  F12.8 deg     RAdeg    *? alpha, degrees (ICRS, Epoch=J1991.25)   (H8)
 5    9        65- 76  F12.8 deg     DEdeg    *? delta, degrees (ICRS, Epoch=J1991.25)   (H9)
 6    10           78  A1    ---     AstroRef *[*+A-Z] Reference flag for astrometry    (H10)
 7    11       80- 86  F7.2  mas     Plx       ? Trigonometric parallax                 (H11)
 8    12       88- 95  F8.2 mas/yr   pmRA     *? Proper motion mu_alpha.cos(delta), ICRS(H12)
 9    13       97-104  F8.2 mas/yr   pmDE     *? Proper motion mu_delta, ICRS           (H13)
10    32      218-223  F6.3  mag     BTmag     ? Mean BT magnitude                      (H32)
11    34      231-236  F6.3  mag     VTmag     ? Mean VT magnitude                      (H34)
12    36          244  A1    ---   m_BTmag    *[A-Z*-] Reference flag for BT and VTmag  (H36)
13    37      246-251  F6.3  mag     B-V       ? Johnson B-V colour                     (H37)
14    44      275-281  F7.4  mag     Hpmag    *? Median magnitude in Hipparcos system   (H44)
15    49      302-306  F5.2  mag     Hpmax     ? Hpmag at maximum (5th percentile)      (H49)
16    50      308-312  F5.2  mag     HPmin     ? Hpmag at minimum (95th percentile)     (H50)
17    51      314-320  F7.2  d       Period    ? Variability period (days)              (H51)
18    52          322  A1    ---     HvarType *[CDMPRU]? variability type               (H52)
19    55      328-337  A10   ---     CCDM      CCDM identifier                          (H55)
20    63      356-358  I3    deg     theta     ? Position angle between components      (H63)
21    64      360-366  F7.3  arcsec  rho       ? Angular separation between components  (H64)
22    66      374-378  F5.2  mag     dHp       ? Magnitude difference of components     (H66)
23    71      391-396  I6    ---     HD        [1/359083]? HD number <III/135>          (H71)
24    72      398-407  A10   ---     BD        Bonner DM <I/119>, <I/122>               (H72)
25    73      409-418  A10   ---     CoD       Cordoba Durchmusterung (DM) <I/114>      (H73)
26    74      420-429  A10   ---     CPD       Cape Photographic DM <I/108>             (H74)
