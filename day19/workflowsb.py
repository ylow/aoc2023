from ranges import *
from dictrange import *
def f_qbl(inrange):
    print('qbl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1574, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_spp(inrange):
    print('spp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2917, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_znm(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3411, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_hqz(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=3171, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_sm(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_mt(subrange)
    return acceptcount
def f_hr(inrange):
    print('hr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2184, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_ts(inrange):
    print('ts',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=252, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=371, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3579, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_fn(subrange)
    return acceptcount
def f_jqx(inrange):
    print('jqx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2040, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_csq(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_nxz(subrange)
    return acceptcount
def f_qft(inrange):
    print('qft',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2939, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_nm(inrange):
    print('nm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2683, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_stf(inrange):
    print('stf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3354, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3146, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_rxb(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_sz(inrange):
    print('sz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1324, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_csh(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1102, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_qhv(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_smb(subrange)
    return acceptcount
def f_qm(inrange):
    print('qm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2419, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_tf(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_fhq(subrange)
    return acceptcount
def f_ln(inrange):
    print('ln',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3452, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_sdc(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3806, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3329, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_mn(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_gtv(subrange)
    return acceptcount
def f_sv(inrange):
    print('sv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2846, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=805, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_mrb(inrange):
    print('mrb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=892, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_jtg(inrange):
    print('jtg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1009, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_pkt(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3010, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_lzx(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_sp(subrange)
    return acceptcount
def f_jq(inrange):
    print('jq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3362, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_pk(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3274, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_zxr(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_sjh(subrange)
    return acceptcount
def f_vhl(inrange):
    print('vhl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3085, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_lgm(inrange):
    print('lgm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1828, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1467, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2175, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_pkh(inrange):
    print('pkh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2156, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1190, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_mtk(inrange):
    print('mtk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=339, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=545, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_vf(inrange):
    print('vf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3575, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_gn(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_bzr(subrange)
    return acceptcount
def f_rlr(inrange):
    print('rlr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2506, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_pkh(subrange)
    return acceptcount
def f_zq(inrange):
    print('zq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=892, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_jcv(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_vp(inrange):
    print('vp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3837, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_zj(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=702, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_hh(inrange):
    print('hh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3225, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_thg(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_sjz(subrange)
    return acceptcount
def f_lfg(inrange):
    print('lfg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3773, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_dbb(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=721, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_ppq(subrange)
    return acceptcount
def f_zcl(inrange):
    print('zcl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1277, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1478, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_mxn(inrange):
    print('mxn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3702, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_zss(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2616, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1078, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_vhh(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_ng(inrange):
    print('ng',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1410, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_qc(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3268, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_fv(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3580, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_tn(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_lfg(subrange)
    return acceptcount
def f_tcq(inrange):
    print('tcq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3342, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2914, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3111, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_js(inrange):
    print('js',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2628, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_smq(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2608, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_vhl(subrange)
    return acceptcount
def f_qp(inrange):
    print('qp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1594, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1781, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_sxj(inrange):
    print('sxj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=387, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1853, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_rdk(inrange):
    print('rdk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1026, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_rtm(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_xq(subrange)
    return acceptcount
def f_zh(inrange):
    print('zh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=889, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_bxn(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_qpb(subrange)
    return acceptcount
def f_hz(inrange):
    print('hz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2951, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_chm(inrange):
    print('chm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3403, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3456, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_tmh(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_rds(inrange):
    print('rds',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2494, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_nk(inrange):
    print('nk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1558, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zv(inrange):
    print('zv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1894, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_fqt(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_lrt(subrange)
    return acceptcount
def f_rb(inrange):
    print('rb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1278, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_zvr(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1005, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_lr(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=621, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_hk(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_gq(subrange)
    return acceptcount
def f_jxq(inrange):
    print('jxq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3571, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_lgq(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=720, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_xf(inrange):
    print('xf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2719, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_pj(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2885, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_hfd(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_ctj(subrange)
    return acceptcount
def f_klx(inrange):
    print('klx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3699, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3744, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3898, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_fgr(inrange):
    print('fgr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3061, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3000, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_bzx(inrange):
    print('bzx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3605, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_gkz(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3474, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_mpt(subrange)
    return acceptcount
def f_lh(inrange):
    print('lh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2838, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2364, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3340, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_cm(inrange):
    print('cm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2481, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_jkn(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2949, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_szf(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3313, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_zkv(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_zv(subrange)
    return acceptcount
def f_ddv(inrange):
    print('ddv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2893, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_bn(inrange):
    print('bn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3160, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3364, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_rbq(inrange):
    print('rbq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1335, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=1190, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2922, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_zht(inrange):
    print('zht',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2105, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=2964, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2355, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_qpb(inrange):
    print('qpb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1387, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2729, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_fvz(inrange):
    print('fvz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2841, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=1023, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_hzm(inrange):
    print('hzm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1472, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=832, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=1216, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_ssz(inrange):
    print('ssz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3330, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_glv(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_nh(inrange):
    print('nh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2958, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_lhn(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_htg(subrange)
    return acceptcount
def f_dvb(inrange):
    print('dvb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=814, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_frh(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=3522, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_chm(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_gfb(subrange)
    return acceptcount
def f_xjg(inrange):
    print('xjg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2980, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_cxt(inrange):
    print('cxt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2875, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2821, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_ngt(inrange):
    print('ngt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1276, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_hj(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1582, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_llm(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1387, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_nxp(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_tnn(subrange)
    return acceptcount
def f_lgr(inrange):
    print('lgr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1156, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2652, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2752, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_gls(inrange):
    print('gls',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1517, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_vdr(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3140, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_cr(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_dkt(inrange):
    print('dkt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3070, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_sqp(inrange):
    print('sqp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3128, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3717, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_trm(inrange):
    print('trm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3807, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3932, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2867, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_fxv(inrange):
    print('fxv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3060, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3872, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3957, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_sc(inrange):
    print('sc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2545, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_crq(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_mkl(subrange)
    return acceptcount
def f_tf(inrange):
    print('tf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2267, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_nhb(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1269, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_rdk(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2660, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_xmg(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_hd(subrange)
    return acceptcount
def f_bmk(inrange):
    print('bmk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2909, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_ff(inrange):
    print('ff',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=166, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1657, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=203, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_ddg(inrange):
    print('ddg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3171, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_vkz(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2032, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_hnj(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_sgv(subrange)
    return acceptcount
def f_kvk(inrange):
    print('kvk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=730, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_qb(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2582, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1642, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_vdr(inrange):
    print('vdr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=732, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zbc(inrange):
    print('zbc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3491, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3354, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_mq(inrange):
    print('mq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=879, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3182, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_kz(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_kh(inrange):
    print('kh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3303, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_sn(inrange):
    print('sn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3085, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=3638, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3223, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_fx(inrange):
    print('fx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3365, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3768, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2290, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zl(inrange):
    print('zl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1180, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_srj(inrange):
    print('srj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2766, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_sjz(inrange):
    print('sjz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2925, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=904, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2888, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_pcb(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_bdj(subrange)
    return acceptcount
def f_fq(inrange):
    print('fq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3351, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_nh(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=964, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_hjh(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1387, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_gtg(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_hz(subrange)
    return acceptcount
def f_crb(inrange):
    print('crb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1900, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=970, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3511, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zx(inrange):
    print('zx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1529, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_cn(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_mr(subrange)
    return acceptcount
def f_fz(inrange):
    print('fz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=853, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_cl(inrange):
    print('cl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3570, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_nf(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3104, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_jn(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_xsj(inrange):
    print('xsj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1327, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_gz(inrange):
    print('gz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2087, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_xt(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2786, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_phh(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_jxq(subrange)
    return acceptcount
def f_sr(inrange):
    print('sr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=686, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_nsx(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2475, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_dv(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_rc(subrange)
    return acceptcount
def f_gv(inrange):
    print('gv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1324, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_rnf(inrange):
    print('rnf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=360, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_vg(subrange)
    return acceptcount
def f_ljq(inrange):
    print('ljq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2095, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=1982, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2041, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_sq(inrange):
    print('sq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2885, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_rlp(inrange):
    print('rlp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3714, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_mxn(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_rq(subrange)
    return acceptcount
def f_hfd(inrange):
    print('hfd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3346, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_nj(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_nd(inrange):
    print('nd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=920, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_hnj(inrange):
    print('hnj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2808, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2971, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3552, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_jlm(inrange):
    print('jlm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3824, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_xck(inrange):
    print('xck',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2449, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_jc(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1262, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_jgl(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=736, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_qbl(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_znr(subrange)
    return acceptcount
def f_jjn(inrange):
    print('jjn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2086, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_lt(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_krr(subrange)
    return acceptcount
def f_jp(inrange):
    print('jp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2407, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_bkh(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_gkj(subrange)
    return acceptcount
def f_szf(inrange):
    print('szf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3345, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_lfj(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3306, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_rlp(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2761, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_zrq(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_rfr(subrange)
    return acceptcount
def f_qvt(inrange):
    print('qvt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2876, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=908, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=766, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_pfn(inrange):
    print('pfn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3150, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=268, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=465, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_kq(inrange):
    print('kq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3578, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_ld(inrange):
    print('ld',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=632, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_rb(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_jq(subrange)
    return acceptcount
def f_fg(inrange):
    print('fg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1947, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_gd(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2011, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_pcb(inrange):
    print('pcb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3005, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2426, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_mqv(inrange):
    print('mqv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2651, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zp(inrange):
    print('zp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3217, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_bpr(inrange):
    print('bpr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3504, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2171, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_nks(inrange):
    print('nks',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2655, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_nx(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2777, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_sl(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_jzt(subrange)
    return acceptcount
def f_zxr(inrange):
    print('zxr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3230, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_lvt(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_lzx(inrange):
    print('lzx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2988, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3006, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_pb(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_mqv(subrange)
    return acceptcount
def f_hqz(inrange):
    print('hqz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=910, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_sqp(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3760, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=3608, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_klp(subrange)
    return acceptcount
def f_zrq(inrange):
    print('zrq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1965, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_xlf(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_hgj(subrange)
    return acceptcount
def f_gff(inrange):
    print('gff',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3296, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3091, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3604, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_lzz(subrange)
    return acceptcount
def f_sp(inrange):
    print('sp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3082, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_dgp(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3562, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_vck(inrange):
    print('vck',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3564, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1343, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_tc(inrange):
    print('tc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2801, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_cnn(inrange):
    print('cnn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=836, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_ggb(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=2366, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_srz(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_kxz(subrange)
    return acceptcount
def f_vm(inrange):
    print('vm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3067, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_ffl(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1054, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_klp(inrange):
    print('klp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1643, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3100, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zs(inrange):
    print('zs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2623, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_prv(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_xsq(inrange):
    print('xsq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3078, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3368, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_ggb(inrange):
    print('ggb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3799, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_ndv(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=1843, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_lcv(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2735, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_gv(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_fth(subrange)
    return acceptcount
def f_smq(inrange):
    print('smq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1630, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3389, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=889, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_jlf(inrange):
    print('jlf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2601, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_qq(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_mkl(inrange):
    print('mkl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1824, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_xcv(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1755, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_zx(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2924, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_xh(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_lg(subrange)
    return acceptcount
def f_jkn(inrange):
    print('jkn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1538, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_dqd(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2181, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_dvb(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_lq(subrange)
    return acceptcount
def f_frh(inrange):
    print('frh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=451, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_hv(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=3680, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_svr(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2584, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_zk(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_lpc(inrange):
    print('lpc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2220, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_nvs(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2723, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_qlh(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_nvq(subrange)
    return acceptcount
def f_xpr(inrange):
    print('xpr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2224, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_hbz(inrange):
    print('hbz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=742, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2908, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=407, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_ghb(inrange):
    print('ghb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=735, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_zf(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=1232, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_bq(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_sr(subrange)
    return acceptcount
def f_qr(inrange):
    print('qr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1056, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_kf(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2726, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2659, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_xsj(subrange)
    return acceptcount
def f_ljg(inrange):
    print('ljg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3202, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_lt(inrange):
    print('lt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3783, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2991, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_znx(subrange)
    return acceptcount
def f_lf(inrange):
    print('lf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2866, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_nkc(inrange):
    print('nkc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2896, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_jjj(inrange):
    print('jjj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1170, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_vcp(inrange):
    print('vcp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3476, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=1527, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_cs(inrange):
    print('cs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2769, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_xk(inrange):
    print('xk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1429, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_xj(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3451, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_dqf(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=864, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_fhd(subrange)
    return acceptcount
def f_csq(inrange):
    print('csq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=133, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3174, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2646, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_cjf(inrange):
    print('cjf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2500, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2966, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2537, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_pch(inrange):
    print('pch',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3402, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=3970, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_dzb(inrange):
    print('dzb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1629, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_lch(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3070, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1344, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_vcg(subrange)
    return acceptcount
def f_pkt(inrange):
    print('pkt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1118, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=1245, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_kqz(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=2841, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_pcp(subrange)
    return acceptcount
def f_qtr(inrange):
    print('qtr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1871, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_nd(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1665, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=1246, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_nc(inrange):
    print('nc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1646, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_mrb(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1348, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_gr(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2803, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_np(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_tfx(subrange)
    return acceptcount
def f_xcq(inrange):
    print('xcq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3438, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_lq(inrange):
    print('lq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3504, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_pt(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_zq(subrange)
    return acceptcount
def f_ljs(inrange):
    print('ljs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2509, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_kxz(inrange):
    print('kxz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3295, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_hcv(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=456, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_ts(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=593, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_vck(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_vp(subrange)
    return acceptcount
def f_ccd(inrange):
    print('ccd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3532, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_jvl(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2141, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_xdb(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_csf(subrange)
    return acceptcount
def f_zzk(inrange):
    print('zzk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2448, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_ffg(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_rnf(subrange)
    return acceptcount
def f_ksf(inrange):
    print('ksf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=252, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_jqx(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2045, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_nks(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3221, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_xgp(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_msk(subrange)
    return acceptcount
def f_tb(inrange):
    print('tb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=884, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3121, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=868, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_mpt(inrange):
    print('mpt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1121, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2693, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_xxp(inrange):
    print('xxp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2396, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2746, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3081, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_zf(inrange):
    print('zf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2583, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_ssz(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1125, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_mx(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_dq(subrange)
    return acceptcount
def f_ltt(inrange):
    print('ltt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1914, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_jk(inrange):
    print('jk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2586, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_vhh(inrange):
    print('vhh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3465, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3842, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zcc(inrange):
    print('zcc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3452, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1752, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_mp(inrange):
    print('mp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2083, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_xq(inrange):
    print('xq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=435, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_rr(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_xh(inrange):
    print('xh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3037, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_spp(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1334, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_ddg(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=463, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_jtg(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_ft(subrange)
    return acceptcount
def f_jzr(inrange):
    print('jzr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2421, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_xs(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_ml(subrange)
    return acceptcount
def f_gr(inrange):
    print('gr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2740, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_qvt(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1030, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_sx(subrange)
    return acceptcount
def f_jzt(inrange):
    print('jzt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2287, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2424, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_pqv(inrange):
    print('pqv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=562, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=514, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_tk(inrange):
    print('tk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2906, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_zm(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_tv(inrange):
    print('tv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2090, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_hvc(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=660, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_rbg(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_bpk(subrange)
    return acceptcount
def f_ll(inrange):
    print('ll',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2966, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=3296, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3419, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_ddv(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_tcq(subrange)
    return acceptcount
def f_ssd(inrange):
    print('ssd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1230, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_ch(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3227, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_vb(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3339, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_xr(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_hbz(subrange)
    return acceptcount
def f_mck(inrange):
    print('mck',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=997, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_mtk(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_ssg(subrange)
    return acceptcount
def f_mbm(inrange):
    print('mbm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3035, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2993, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3381, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_knc(inrange):
    print('knc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=717, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_nj(inrange):
    print('nj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3662, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_kt(inrange):
    print('kt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1393, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_zm(inrange):
    print('zm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3077, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1102, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_xp(inrange):
    print('xp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=555, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=686, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_kcz(inrange):
    print('kcz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=958, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3307, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_lch(inrange):
    print('lch',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2420, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_lsg(inrange):
    print('lsg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=841, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2937, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_lgg(inrange):
    print('lgg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3631, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_zkg(subrange)
    return acceptcount
def f_dt(inrange):
    print('dt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2282, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1907, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_nxz(inrange):
    print('nxz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2740, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2788, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3169, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_ml(inrange):
    print('ml',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3641, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_fk(inrange):
    print('fk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3560, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_bkh(inrange):
    print('bkh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3566, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_gks(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_vd(inrange):
    print('vd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=821, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_zkv(inrange):
    print('zkv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2074, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_vf(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_gz(subrange)
    return acceptcount
def f_txl(inrange):
    print('txl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2986, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_xj(inrange):
    print('xj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1331, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=607, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_kf(inrange):
    print('kf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=649, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_zk(inrange):
    print('zk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=899, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2066, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_lvs(inrange):
    print('lvs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=705, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=872, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3101, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_bpk(inrange):
    print('bpk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2727, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_zzk(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1544, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_vc(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3548, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_jjn(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_zbt(subrange)
    return acceptcount
def f_znm(inrange):
    print('znm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2638, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1174, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_rs(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_fb(inrange):
    print('fb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2811, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_xrx(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=1973, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_xl(inrange):
    print('xl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3521, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_lrt(inrange):
    print('lrt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3626, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_hc(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_tj(subrange)
    return acceptcount
def f_rfr(inrange):
    print('rfr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2578, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_xc(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3692, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_gxf(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_nm(subrange)
    return acceptcount
def f_cv(inrange):
    print('cv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3435, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2464, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3715, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_dm(inrange):
    print('dm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2201, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_nhb(inrange):
    print('nhb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1451, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_fg(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_bj(subrange)
    return acceptcount
def f_in(inrange):
    print('in',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2577, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_xx(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3180, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_gj(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_sc(subrange)
    return acceptcount
def f_rhg(inrange):
    print('rhg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1974, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2182, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=829, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_lg(inrange):
    print('lg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2525, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_hb(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1244, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_lpc(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=658, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_ksf(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_nz(subrange)
    return acceptcount
def f_jd(inrange):
    print('jd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2179, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_zp(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1381, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_spr(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=1732, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_txp(inrange):
    print('txp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1927, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_cv(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_kb(subrange)
    return acceptcount
def f_jr(inrange):
    print('jr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1781, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1902, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_hd(inrange):
    print('hd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1750, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_kt(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_rgg(subrange)
    return acceptcount
def f_gxf(inrange):
    print('gxf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3755, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_nk(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=2695, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_frz(inrange):
    print('frz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1759, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3233, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=654, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_dz(inrange):
    print('dz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1223, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2655, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=644, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_htg(inrange):
    print('htg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3741, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3868, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3045, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_gks(inrange):
    print('gks',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3093, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3813, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3256, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_lzz(inrange):
    print('lzz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2999, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=2878, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3038, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_bpf(inrange):
    print('bpf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3163, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zgd(inrange):
    print('zgd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1196, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1317, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_vg(inrange):
    print('vg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2455, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2304, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=541, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_bcf(inrange):
    print('bcf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=348, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=191, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_pxv(inrange):
    print('pxv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3389, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=146, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=67, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_pg(inrange):
    print('pg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2806, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=3213, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=272, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_sh(inrange):
    print('sh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3146, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2832, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1900, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_nz(inrange):
    print('nz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2724, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_tjh(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3242, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_lgg(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_jhc(subrange)
    return acceptcount
def f_fqt(inrange):
    print('fqt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3693, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_srj(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_mnv(subrange)
    return acceptcount
def f_xpf(inrange):
    print('xpf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2849, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_kq(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=1701, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_qtq(subrange)
    return acceptcount
def f_nqx(inrange):
    print('nqx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=160, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_xpr(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_qv(subrange)
    return acceptcount
def f_xc(inrange):
    print('xc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2525, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_ljs(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2083, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_klx(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1150, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_hqg(subrange)
    return acceptcount
def f_hc(inrange):
    print('hc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2344, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_crb(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zj(inrange):
    print('zj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=717, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=1865, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_tp(inrange):
    print('tp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2510, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_zxn(inrange):
    print('zxn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=912, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3357, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_sgv(inrange):
    print('sgv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2978, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_gqv(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3171, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_mh(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_phh(inrange):
    print('phh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=742, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_lmb(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1213, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_sn(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3030, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_ltt(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_ndv(inrange):
    print('ndv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2330, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_tg(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_gfc(subrange)
    return acceptcount
def f_csf(inrange):
    print('csf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1891, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_jj(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3261, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_nhd(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_npf(subrange)
    return acceptcount
def f_dbb(inrange):
    print('dbb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=481, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=844, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_rs(inrange):
    print('rs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3107, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1855, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=2229, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_gzd(inrange):
    print('gzd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1744, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=633, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_qc(inrange):
    print('qc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2912, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_tb(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=854, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_kxs(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_xs(inrange):
    print('xs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2120, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_sl(inrange):
    print('sl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3478, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_dn(inrange):
    print('dn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=895, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_lzj(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_tk(subrange)
    return acceptcount
def f_cb(inrange):
    print('cb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=858, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=825, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=677, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zss(inrange):
    print('zss',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3545, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3827, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=3685, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_cn(inrange):
    print('cn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2843, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_qr(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=1074, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_kg(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_zfd(subrange)
    return acceptcount
def f_xrx(inrange):
    print('xrx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2168, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=611, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_gq(inrange):
    print('gq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3302, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_jl(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3237, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_pg(subrange)
    return acceptcount
def f_zkg(inrange):
    print('zkg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2049, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=1016, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3848, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_vbb(inrange):
    print('vbb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3464, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_lgq(inrange):
    print('lgq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3381, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=1089, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_cf(inrange):
    print('cf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=863, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_xp(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_bjl(inrange):
    print('bjl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1676, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_xg(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3264, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_cf(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2873, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_gl(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_cg(subrange)
    return acceptcount
def f_jl(inrange):
    print('jl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2645, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2272, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_gkj(inrange):
    print('gkj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3097, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_lh(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3723, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_fxv(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_hgx(inrange):
    print('hgx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2317, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_zh(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_bz(subrange)
    return acceptcount
def f_gl(inrange):
    print('gl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=669, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_rm(subrange)
    return acceptcount
def f_jc(inrange):
    print('jc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=940, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_zc(inrange):
    print('zc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3283, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_vn(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2491, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_dd(subrange)
    return acceptcount
def f_mk(inrange):
    print('mk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=932, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2605, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_qft(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2591, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_rrb(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_lm(inrange):
    print('lm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3182, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=807, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_crq(inrange):
    print('crq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1950, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_fpb(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_vzs(subrange)
    return acceptcount
def f_ft(inrange):
    print('ft',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=228, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_vs(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=362, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_txl(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_qhh(subrange)
    return acceptcount
def f_qmn(inrange):
    print('qmn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3417, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=724, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1577, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_rmg(subrange)
    return acceptcount
def f_ffb(inrange):
    print('ffb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3279, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_rlr(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_xpf(subrange)
    return acceptcount
def f_zfd(inrange):
    print('zfd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=612, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=1076, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_dtq(inrange):
    print('dtq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2745, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_bzr(inrange):
    print('bzr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3390, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_bp(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_kr(inrange):
    print('kr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3517, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_cnn(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=1807, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_ghb(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2518, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_cj(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_ld(subrange)
    return acceptcount
def f_gj(inrange):
    print('gj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1613, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_kr(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_cm(subrange)
    return acceptcount
def f_mt(inrange):
    print('mt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3132, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_dnh(subrange)
    return acceptcount
def f_nvs(inrange):
    print('nvs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1916, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_qrt(inrange):
    print('qrt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3293, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=244, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=2764, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_tjh(inrange):
    print('tjh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3024, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3504, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_kcz(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2172, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_tc(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_fvz(subrange)
    return acceptcount
def f_xcv(inrange):
    print('xcv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=853, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_mck(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2933, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_bvq(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1527, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_ngt(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_sz(subrange)
    return acceptcount
def f_lgs(inrange):
    print('lgs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3122, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_zg(inrange):
    print('zg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3119, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_jr(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_zcc(subrange)
    return acceptcount
def f_znx(inrange):
    print('znx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=821, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=407, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_bp(inrange):
    print('bp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1466, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2822, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2517, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_dd(inrange):
    print('dd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2900, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_rbg(inrange):
    print('rbg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2594, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_nc(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_hh(subrange)
    return acceptcount
def f_kc(inrange):
    print('kc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=228, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_nts(inrange):
    print('nts',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2171, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_nl(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_ds(subrange)
    return acceptcount
def f_sjh(inrange):
    print('sjh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=262, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3320, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_kh(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_fv(inrange):
    print('fv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=974, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1329, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_vd(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1154, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_dz(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_dtq(subrange)
    return acceptcount
def f_np(inrange):
    print('np',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2901, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_zxn(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1894, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2229, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_xn(subrange)
    return acceptcount
def f_mr(inrange):
    print('mr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2671, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_lfb(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2379, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_fb(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2568, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_mk(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_tz(subrange)
    return acceptcount
def f_hfv(inrange):
    print('hfv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1246, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_gls(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=1496, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_jzz(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_zg(subrange)
    return acceptcount
def f_zmx(inrange):
    print('zmx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3168, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_ff(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_vkz(inrange):
    print('vkz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2647, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2206, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_fth(inrange):
    print('fth',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3911, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_bjg(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_pch(subrange)
    return acceptcount
def f_jn(inrange):
    print('jn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3853, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3385, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_sd(inrange):
    print('sd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3775, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2449, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_cz(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=405, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_rnz(subrange)
    return acceptcount
def f_qv(inrange):
    print('qv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1021, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2252, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_ffl(inrange):
    print('ffl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1027, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_zzs(inrange):
    print('zzs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1866, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3209, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3609, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_hsf(inrange):
    print('hsf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1476, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_thg(inrange):
    print('thg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3652, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3508, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1068, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_hr(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_mzk(subrange)
    return acceptcount
def f_kg(inrange):
    print('kg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2965, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_lvs(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2887, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2860, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_bpf(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_pqv(subrange)
    return acceptcount
def f_nx(inrange):
    print('nx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2779, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2164, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=438, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_md(inrange):
    print('md',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=701, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3344, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_cth(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2599, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_qrt(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_bcf(subrange)
    return acceptcount
def f_xx(inrange):
    print('xx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1273, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_qm(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_tv(subrange)
    return acceptcount
def f_gtv(inrange):
    print('gtv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3261, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_nq(inrange):
    print('nq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2860, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_hp(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_tz(inrange):
    print('tz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=689, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_jjj(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=372, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_cjf(subrange)
    return acceptcount
def f_srz(inrange):
    print('srz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=331, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_nqx(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1166, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_sd(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_bx(subrange)
    return acceptcount
def f_nf(inrange):
    print('nf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2077, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3322, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_mh(inrange):
    print('mh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3013, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2292, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2375, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_qzt(inrange):
    print('qzt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=938, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2719, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=1478, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_kb(inrange):
    print('kb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3541, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_lvt(inrange):
    print('lvt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2737, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3246, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_qlh(inrange):
    print('qlh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2051, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_vll(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_vn(inrange):
    print('vn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2909, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_rtm(inrange):
    print('rtm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1680, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_bfv(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_jzh(inrange):
    print('jzh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3240, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3271, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3499, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_ssg(inrange):
    print('ssg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2380, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_lf(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=370, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_glv(inrange):
    print('glv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1131, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_bkf(inrange):
    print('bkf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2591, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2676, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=350, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_xhx(inrange):
    print('xhx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=855, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=766, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_bqg(inrange):
    print('bqg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3272, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3214, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3112, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_bc(inrange):
    print('bc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=156, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=934, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2168, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_rl(inrange):
    print('rl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3333, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=2865, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_cth(inrange):
    print('cth',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=397, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_rx(inrange):
    print('rx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1610, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3500, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2000, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_tj(inrange):
    print('tj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=979, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_rp(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_prm(inrange):
    print('prm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3770, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_fhd(inrange):
    print('fhd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1529, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_rdq(inrange):
    print('rdq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3743, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3890, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3836, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_svr(inrange):
    print('svr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1277, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_rxb(inrange):
    print('rxb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2065, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=619, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_jkm(inrange):
    print('jkm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2967, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_npf(inrange):
    print('npf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2238, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_hgj(inrange):
    print('hgj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3122, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3097, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_jkm(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3627, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_lv(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_mx(inrange):
    print('mx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1554, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_pfn(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=437, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_pxv(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3296, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_tfx(inrange):
    print('tfx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=992, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=1093, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_pq(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2544, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_lgr(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_pq(inrange):
    print('pq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2392, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_vcg(inrange):
    print('vcg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1038, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=499, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_bq(inrange):
    print('bq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3320, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_xk(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_kvk(subrange)
    return acceptcount
def f_mzk(inrange):
    print('mzk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3568, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=853, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_kbk(inrange):
    print('kbk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3343, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_lhn(inrange):
    print('lhn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2868, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=838, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_cql(inrange):
    print('cql',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=732, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_nvq(inrange):
    print('nvq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2634, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_zht(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_hqg(inrange):
    print('hqg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2554, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_rrb(inrange):
    print('rrb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2127, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2881, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_gqt(inrange):
    print('gqt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2499, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2623, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3424, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_csh(inrange):
    print('csh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=624, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=1599, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_tt(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1434, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_pnk(inrange):
    print('pnk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2982, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3177, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_xg(inrange):
    print('xg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3449, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_sh(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1459, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3790, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_hq(subrange)
    return acceptcount
def f_gd(inrange):
    print('gd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=763, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1542, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_gtg(inrange):
    print('gtg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1721, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_pnk(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1544, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_fgr(subrange)
    return acceptcount
def f_jcv(inrange):
    print('jcv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2830, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3291, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_hrh(inrange):
    print('hrh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3490, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_jlm(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_mp(subrange)
    return acceptcount
def f_bxn(inrange):
    print('bxn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3078, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_xbb(inrange):
    print('xbb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3000, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=2557, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3329, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_jzn(inrange):
    print('jzn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2306, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2986, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2949, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_cbz(inrange):
    print('cbz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2452, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2653, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2537, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zbt(inrange):
    print('zbt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=273, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_ms(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=109, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_zmx(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_hpb(subrange)
    return acceptcount
def f_ctj(inrange):
    print('ctj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1790, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_frz(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2123, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_mbm(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_pcp(inrange):
    print('pcp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3380, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1195, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2990, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_jhc(inrange):
    print('jhc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2482, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_jsx(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_cz(inrange):
    print('cz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=653, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3649, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_bfv(inrange):
    print('bfv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=548, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=638, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=396, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_spr(inrange):
    print('spr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3678, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=1552, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1735, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_vr(inrange):
    print('vr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3020, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_ms(inrange):
    print('ms',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2429, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3099, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=425, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_nkc(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_rl(subrange)
    return acceptcount
def f_tnn(inrange):
    print('tnn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3093, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_qtq(inrange):
    print('qtq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=912, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=597, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_jct(inrange):
    print('jct',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3362, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1030, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=883, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_bvq(inrange):
    print('bvq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1295, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_dzb(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_jtp(subrange)
    return acceptcount
def f_lls(inrange):
    print('lls',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2726, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2507, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2648, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_tn(inrange):
    print('tn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=951, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_nrz(subrange)
    return acceptcount
def f_cr(inrange):
    print('cr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1004, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1025, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_vll(inrange):
    print('vll',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2293, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2192, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_dv(inrange):
    print('dv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1039, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_jm(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_tt(inrange):
    print('tt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=862, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_lcv(inrange):
    print('lcv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1479, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3886, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_zl(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=952, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_rv(subrange)
    return acceptcount
def f_gt(inrange):
    print('gt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1480, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_jfs(subrange)
    return acceptcount
def f_gqv(inrange):
    print('gqv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3635, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_kqz(inrange):
    print('kqz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3214, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_sx(inrange):
    print('sx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=787, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_tg(inrange):
    print('tg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1450, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3694, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1757, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_hvc(inrange):
    print('hvc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=578, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_xck(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2269, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_hfv(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_ng(subrange)
    return acceptcount
def f_mg(inrange):
    print('mg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1565, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_lvq(inrange):
    print('lvq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3284, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3217, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_krr(inrange):
    print('krr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3777, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_kc(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=239, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_hb(inrange):
    print('hb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2694, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_js(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_vm(subrange)
    return acceptcount
def f_bx(inrange):
    print('bx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1924, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_ljq(subrange)
    return acceptcount
def f_jzz(inrange):
    print('jzz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1738, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_cb(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=901, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_xhx(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1962, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_rr(inrange):
    print('rr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=896, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_qcg(inrange):
    print('qcg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2516, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_kxs(inrange):
    print('kxs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=840, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=747, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1356, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_lfj(inrange):
    print('lfj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2038, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_zb(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3166, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_gff(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3183, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_xl(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_cc(subrange)
    return acceptcount
def f_gqd(inrange):
    print('gqd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=864, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2993, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=3181, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_dkd(inrange):
    print('dkd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2780, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=441, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_bjf(inrange):
    print('bjf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1394, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2548, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_ch(inrange):
    print('ch',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3354, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_xjg(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_bmk(subrange)
    return acceptcount
def f_vc(inrange):
    print('vc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=267, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_txp(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=173, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_gt(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_jlf(subrange)
    return acceptcount
def f_jx(inrange):
    print('jx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=256, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_lgm(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_gfb(inrange):
    print('gfb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3822, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2902, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_zgd(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3888, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_cbz(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_pk(inrange):
    print('pk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1524, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2065, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3212, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_ffr(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_sm(inrange):
    print('sm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=974, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_pbr(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_jgl(inrange):
    print('jgl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2296, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_zcl(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=914, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_zzs(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=482, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_gzd(subrange)
    return acceptcount
def f_nhd(inrange):
    print('nhd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3391, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_rm(inrange):
    print('rm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2052, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_hpb(inrange):
    print('hpb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=65, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3263, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_cql(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=699, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_sxj(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_dkt(subrange)
    return acceptcount
def f_xmg(inrange):
    print('xmg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1190, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_sk(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=652, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_jx(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2015, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_qtr(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_kp(subrange)
    return acceptcount
def f_fvb(inrange):
    print('fvb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2321, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3359, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_gqk(inrange):
    print('gqk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2630, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_zvr(inrange):
    print('zvr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1828, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3360, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_bqg(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2878, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_vbb(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_tp(subrange)
    return acceptcount
def f_cc(inrange):
    print('cc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3643, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_trm(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_bn(subrange)
    return acceptcount
def f_qj(inrange):
    print('qj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3458, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_mq(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_ln(subrange)
    return acceptcount
def f_pb(inrange):
    print('pb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2589, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2846, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=652, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_kz(inrange):
    print('kz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3313, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_fhq(inrange):
    print('fhq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2306, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_bjl(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=3115, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_xf(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3112, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_ccd(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_gf(subrange)
    return acceptcount
def f_xdb(inrange):
    print('xdb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1943, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_xbb(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3562, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_xn(inrange):
    print('xn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=892, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3291, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1048, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_dqf(inrange):
    print('dqf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3370, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_jfs(inrange):
    print('jfs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3339, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3124, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_xlf(inrange):
    print('xlf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3542, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_xsq(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_prm(subrange)
    return acceptcount
def f_hq(inrange):
    print('hq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3606, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3671, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_mn(inrange):
    print('mn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3346, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_hj(inrange):
    print('hj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2854, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_fz(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_bjg(inrange):
    print('bjg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1680, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_bz(inrange):
    print('bz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2925, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2864, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_gqt(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_kbk(subrange)
    return acceptcount
def f_llm(inrange):
    print('llm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2811, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_qcg(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2864, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2745, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_dq(inrange):
    print('dq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3350, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_knc(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_lvq(subrange)
    return acceptcount
def f_gn(inrange):
    print('gn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3784, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2766, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_gqk(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_xxp(subrange)
    return acceptcount
def f_vs(inrange):
    print('vs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2568, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_jzn(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2977, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_mnv(inrange):
    print('mnv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2422, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_fk(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3599, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3471, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_qhh(inrange):
    print('qhh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2968, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_ljg(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_msk(inrange):
    print('msk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1922, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_cs(subrange)
    return acceptcount
def f_rnz(inrange):
    print('rnz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=540, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_xgp(inrange):
    print('xgp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1935, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1818, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_dkd(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=1776, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_qhv(inrange):
    print('qhv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=998, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=593, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_hzm(subrange)
    return acceptcount
def f_gf(inrange):
    print('gf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1860, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_nts(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3480, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_nq(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2782, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_jd(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_zs(subrange)
    return acceptcount
def f_nrz(inrange):
    print('nrz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3457, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_pt(inrange):
    print('pt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2776, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_pbr(inrange):
    print('pbr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3065, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3090, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1827, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_zb(inrange):
    print('zb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3484, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_lgs(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3470, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_bv(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_fpb(inrange):
    print('fpb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2199, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_dn(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2822, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_fq(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_ssd(subrange)
    return acceptcount
def f_bv(inrange):
    print('bv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=795, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=510, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_vnf(inrange):
    print('vnf',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1189, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_lv(inrange):
    print('lv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3761, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_hv(inrange):
    print('hv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3464, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_ffg(inrange):
    print('ffg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2301, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_bkf(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_bjf(subrange)
    return acceptcount
def f_sk(inrange):
    print('sk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1830, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_rhg(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=935, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1717, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_qp(subrange)
    return acceptcount
def f_znr(inrange):
    print('znr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=319, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_dj(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=1775, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2856, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_xcq(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_bc(subrange)
    return acceptcount
def f_jtp(inrange):
    print('jtp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1284, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_bj(inrange):
    print('bj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2041, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_dt(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=2024, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=2936, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_rx(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_rv(inrange):
    print('rv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1140, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=1291, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3930, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_gkz(inrange):
    print('gkz',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3746, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=2666, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_prv(inrange):
    print('prv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1656, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1447, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=1940, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_dnh(inrange):
    print('dnh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2788, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_qq(inrange):
    print('qq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=72, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_vb(inrange):
    print('vb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2857, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_rds(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(end=2718, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_dj(inrange):
    print('dj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=419, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=928, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=421, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_rc(inrange):
    print('rc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1146, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_jct(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_bb(inrange):
    print('bb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2075, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_zc(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_bzx(subrange)
    return acceptcount
def f_jm(inrange):
    print('jm',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=919, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_jj(inrange):
    print('jj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1067, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3369, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_smb(inrange):
    print('smb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=645, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_qzt(subrange)
    return acceptcount
def f_lr(inrange):
    print('lr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3337, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_thl(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3276, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3223, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_vr(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_lm(subrange)
    return acceptcount
def f_rq(inrange):
    print('rq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3448, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_rdq(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_nsx(inrange):
    print('nsx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=318, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_fvb(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_jk(subrange)
    return acceptcount
def f_dqd(inrange):
    print('dqd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3010, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_jzr(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3543, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_hrh(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2149, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_qmn(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_cl(subrange)
    return acceptcount
def f_vzs(inrange):
    print('vzs',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3264, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_ffb(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=2813, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_bb(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3004, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_jp(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_hgx(subrange)
    return acceptcount
def f_cg(inrange):
    print('cg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1077, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=680, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=3091, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_thl(inrange):
    print('thl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2939, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=836, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_lfb(inrange):
    print('lfb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3163, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_cxt(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_zbc(subrange)
    return acceptcount
def f_hk(inrange):
    print('hk',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1305, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_lmt(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1042, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=3332, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_jzh(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += f_vnf(subrange)
    return acceptcount
def f_lmb(inrange):
    print('lmb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=392, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3497, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_kp(inrange):
    print('kp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=1605, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_cgx(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=869, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_rmg(inrange):
    print('rmg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3471, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(start=1987, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_cj(inrange):
    print('cj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3154, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_xpd(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_qj(subrange)
    return acceptcount
def f_hjh(inrange):
    print('hjh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=438, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_ndp(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=2990, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    return acceptcount
def f_lzj(inrange):
    print('lzj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3379, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_rbq(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1060, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1413, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_xt(inrange):
    print('xt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3666, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += f_sq(localrange)
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3083, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1802, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_xr(inrange):
    print('xr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2655, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_sv(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=449, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_gqd(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_pj(inrange):
    print('pj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1807, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=3030, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_dm(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += f_fx(subrange)
    return acceptcount
def f_hp(inrange):
    print('hp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3286, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1486, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_ppq(inrange):
    print('ppq',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=374, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_xpd(inrange):
    print('xpd',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2339, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_stf(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=2848, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += f_ll(localrange)
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += f_md(subrange)
    return acceptcount
def f_bdj(inrange):
    print('bdj',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1473, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=2491, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1144, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_fn(inrange):
    print('fn',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3456, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_lmt(inrange):
    print('lmt',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3104, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_sdc(inrange):
    print('sdc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=660, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_qb(inrange):
    print('qb',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3231, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_ds(inrange):
    print('ds',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2355, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_hcv(inrange):
    print('hcv',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=452, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_cgx(inrange):
    print('cgx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=1866, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=1983, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=849, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
def f_ndp(inrange):
    print('ndp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2968, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2909, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_nl(inrange):
    print('nl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2686, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(end=1818, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=3153, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_rp(inrange):
    print('rp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3751, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=1387, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=3721, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_rgg(inrange):
    print('rgg',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=944, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1930, include_end=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += f_vcp(localrange)
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    constraint = Range(start=413, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_mg(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_bpr(subrange)
    return acceptcount
def f_jsx(inrange):
    print('jsx',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=2639, include_end=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(end=2210, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=949, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)

    subrange['m'] = subrange['m'].intersection(constraint.complement())
    return acceptcount
def f_ffr(inrange):
    print('ffr',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3563, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['a'] = subrange['a'].intersection(constraint.complement())
    constraint = Range(start=3419, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=3749, include_start=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_nxp(inrange):
    print('nxp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=571, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_hsf(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1063, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += f_lsg(localrange)
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    constraint = Range(end=1247, include_end=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += f_lls(subrange)
    return acceptcount
def f_tmh(inrange):
    print('tmh',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=2732, include_start=False)
    localrange = subrange.copy()
    localrange['m'] = localrange['m'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['m'] = subrange['m'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_gfc(inrange):
    print('gfc',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3656, include_start=False)
    localrange = subrange.copy()
    localrange['x'] = localrange['x'].intersection(constraint)

    subrange['x'] = subrange['x'].intersection(constraint.complement())
    constraint = Range(start=1835, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)

    subrange['s'] = subrange['s'].intersection(constraint.complement())
    return acceptcount
def f_jvl(inrange):
    print('jvl',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(start=3628, include_start=False)
    localrange = subrange.copy()
    localrange['s'] = localrange['s'].intersection(constraint)
    acceptcount += localrange.length()
    subrange['s'] = subrange['s'].intersection(constraint.complement())
    acceptcount += subrange.length()
    return acceptcount
def f_dgp(inrange):
    print('dgp',inrange)
    subrange = inrange.copy()
    acceptcount = 0
    constraint = Range(end=3391, include_end=False)
    localrange = subrange.copy()
    localrange['a'] = localrange['a'].intersection(constraint)

    subrange['a'] = subrange['a'].intersection(constraint.complement())
    return acceptcount
initial = DictRange()
initial.init_default()
r = f_in(initial)
print(r)
