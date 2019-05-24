def get_files(ftype='activity'):
  """
  Repository of saved data files.
  Model name key:
    - lX = locally restricted connections with width X
    - (S)L = (supra)linear
    - PI = positive input
    - EO = excitatory output only
    - VC = trained with variable contrast images
  """
  s = 'activity_0' if ftype == 'activity' else ftype
  file_dict = {
    'SL': [
        'alexnetRepEI_128FF_nt16_dt2.0_pwr1.9_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Abs_0009v3_{}.pkl'.format(s)
    ],
    'L': [
        'alexnetRepEI_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Abs_0011v3_{}.pkl'.format(s)
    ],
    'l10_L': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd10_0002v4_{}.pkl'.format(s)
    ],
    'l40_SL': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.9_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd40_0011v4_{}.pkl'.format(s)
    ],
    'l40_SL_VC': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd40VC_0013v4_{}.pkl'.format(s)
    ],
    'l20_L_PI': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20PO_0009v4_{}.pkl'.format(s)
    ],
    'l10_L_VC': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd10VC_0007v4_{}.pkl'.format(s)
    ],
    'l25_SL_VC': [
        'alexnetRepEIdd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.04tnorm_FF0.02Mom0.9LR0.01drp30Absdd25VC_0021v4_{}.pkl'.format(s)
    ],
    'l20_L_VC_PI_EO': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20VC2POEO_0019v5_{}.pkl'.format(s)
    ],
    'l20_SL_VC_PI': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20VC2PO_0010v5_{}.pkl'.format(s)
    ],
    'l20_L_VC_PI': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20VC2PO_0013v5_{}.pkl'.format(s)
    ],
    'l20_SL_PI': [
       'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20PO_0011v5_{}.pkl'.format(s)
    ],
    'l20_L_PI': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20PO_0012v5_{}.pkl'.format(s)
    ],
    'l20_SL_VC': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20VC2_0016v5_{}.pkl'.format(s)
    ],
    'l20_L_VC': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.0_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20VC2_0017v5_{}.pkl'.format(s)
    ],
    'l20_SL_VC_PI_EO': [
        'alexnetRepEI5dd_128FF_nt16_dt2.0_pwr1.8_k1.0_EIstd0.02tnorm_FF0.02Mom0.9LR0.01drp30Absdd20VC2POEO_0020v5_{}.pkl'.format(s)
    ]
    
  } 
    
  if ftype == 'weights':
    del file_dict['SL']
    del file_dict['L']
  return file_dict