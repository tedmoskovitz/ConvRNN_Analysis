def get_files(ftype='activity'):
  s = 'activity_0' if ftype == 'activity' else ftype
  file_dict = {
    'supralinear': [
        'alexnetRepEI_128FF_nt16_dt2.0_pwr1.9_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Abs_0009v3_{}.pkl'.format(s)
    ],
    'linear': [
        'alexnetRepEI_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Abs_0011v3_{}.pkl'.format(s)
    ],
    'local10_linear': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd10_0002v4_{}.pkl'.format(s)
    ],
    'local40_supralinear': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.9_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd40_0011v4_{}.pkl'.format(s)
    ],
    'local40_supralinear_VC': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd40VC_0013v4_{}.pkl'.format(s)
    ],
    'local20_linear_posInput': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20PO_0009v4_{}.pkl'.format(s)
    ],
    'local10_linear_VC': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd10VC_0007v4_{}.pkl'.format(s)
    ],
    'local25_supralinear_VC': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.04tnorm_FF0.02Mom0.9LR0.01drp30Absdd25VC_0021v4_{}.pkl'.format(s)
    ],
    'local20_linear_posInput_EOutput': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20VC2POEO_0019v5_{}.pkl'.format(s)
    ],
    'local20_supralinear_VC_posInput': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20VC2PO_0010v5_{}.pkl'.format(s)
    ],
    'local20_linear_VC_posInput': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd40VC_0013v4_{}.pkl'.format(s)
    ],
    'local20_supralinear_posInput': [
       'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20PO_0011v5_{}.pkl'.format(s)
    ],
    'local20_linear_posInput': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20PO_0012v5_{}.pkl'.format(s)
    ],
    'local20_supralinear_VC': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20VC2_0016v5_{}.pkl'.format(s)
    ],
    'local20_linear_VC': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20VC2_0017v5_{}.pkl'.format(s)
    ],
    'local20_supralinear_VC_posInput_EOutput': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20VC2POEO_0020v5_{}.pkl'.format(s)
    ]
    
  } 
    
  if ftype == 'weights':
    del file_dict['supralinear']
    del file_dict['linear']
  return file_dict