#!/usr/bin/python3
from novas import compat as novas

def d2dms(d):
    sign="+"
    if(d<0):
        sign="-"
    
    d=abs(d)
    m=(abs(d)%1) * 60
    s=(abs(m)%1) * 60
    return '%s%02d:%02d:%011.8f' % (sign,d,m,s)

def printstar(star):
    print("%s %s %7.2f %7.2f %7.2f" % (d2dms(star.ra),d2dms(star.dec),star.parallax,star.promodec,star.promora))

def convertstar(name,num,dec,ra,plax,pdec,pra):
    star=novas.CatEntry()
    #star.starname=""
    star.starnumber=int(num)
    star.dec=float(dec)
    star.ra=float(ra)
    star.parallax=float(plax)
    star.promodec=float(pdec)
    star.promora=float(pra)
    #printstar(star)
    s2=novas.transform_hip(star)
    return [s2.ra,s2.dec]

print("hipparcos_catalog=[")
file=open('hip_main.dat')
fail=0;
for l in file:
    f=l.split("|")
    try:
        mag=float(f[5])
        if(mag<100):
            [ra,dec]=convertstar("",f[1],f[9],f[8],f[11],f[13],f[12])
            print("[%s, \"%s\", %s, %s, %12.8f, %12.8f," % (f[1],f[2],f[5],f[6],ra*15,dec),end='')
            print("\"%s\", %s, %s, %s, %s, %s, \"%s\", %s, %s, %s, " % (f[10],f[11],f[12],f[13],f[32],f[34],f[36],f[37],f[44],f[49]),end='')
            print("%s, %s, \"%s\", \"%s\", %s, %s, %s, %s, " % (f[50],f[51],f[52],f[55],f[63],f[64],f[66],f[71]),end="")
            print("\"%s\", \"%s\", \"%s\"]," % (f[72],f[73],f[74]))
    except:
        fail=fail+1 #263 should fail due to missing RA_deg/Dec_deg field

print("];")
print("//Fail: %d" % (fail))


# 1         9- 14  I6    ---     HIP       Identifier (HIP number)                   (H1)
# 2            16  A1    ---     Proxy    *[HT] Proximity flag                       (H2)
# 5        42- 46  F5.2  mag     Vmag      ? Magnitude in Johnson V                  (H5)
# 6            48  I1    ---     VarFlag  *[1,3]? Coarse variability flag            (H6)
# 8        52- 63  F12.8 deg     RAdeg    *? alpha, degrees (ICRS, Epoch=J1991.25)   (H8)
# 9        65- 76  F12.8 deg     DEdeg    *? delta, degrees (ICRS, Epoch=J1991.25)   (H9)
# 10           78  A1    ---     AstroRef *[*+A-Z] Reference flag for astrometry    (H10)
# 11       80- 86  F7.2  mas     Plx       ? Trigonometric parallax                 (H11)
# 12       88- 95  F8.2 mas/yr   pmRA     *? Proper motion mu_alpha.cos(delta), ICRS(H12)
# 13       97-104  F8.2 mas/yr   pmDE     *? Proper motion mu_delta, ICRS           (H13)
# 32      218-223  F6.3  mag     BTmag     ? Mean BT magnitude                      (H32)
# 34      231-236  F6.3  mag     VTmag     ? Mean VT magnitude                      (H34)
# 36          244  A1    ---   m_BTmag    *[A-Z*-] Reference flag for BT and VTmag  (H36)
# 37      246-251  F6.3  mag     B-V       ? Johnson B-V colour                     (H37)
# 44      275-281  F7.4  mag     Hpmag    *? Median magnitude in Hipparcos system   (H44)
# 49      302-306  F5.2  mag     Hpmax     ? Hpmag at maximum (5th percentile)      (H49)
# 50      308-312  F5.2  mag     HPmin     ? Hpmag at minimum (95th percentile)     (H50)
# 51      314-320  F7.2  d       Period    ? Variability period (days)              (H51)
# 52          322  A1    ---     HvarType *[CDMPRU]? variability type               (H52)
# 55      328-337  A10   ---     CCDM      CCDM identifier                          (H55)
# 63      356-358  I3    deg     theta     ? Position angle between components      (H63)
# 64      360-366  F7.3  arcsec  rho       ? Angular separation between components  (H64)
# 66      374-378  F5.2  mag     dHp       ? Magnitude difference of components     (H66)
# 71      391-396  I6    ---     HD        [1/359083]? HD number <III/135>          (H71)
# 72      398-407  A10   ---     BD        Bonner DM <I/119>, <I/122>               (H72)
# 73      409-418  A10   ---     CoD       Cordoba Durchmusterung (DM) <I/114>      (H73)
# 74      420-429  A10   ---     CPD       Cape Photographic DM <I/108>             (H74)
