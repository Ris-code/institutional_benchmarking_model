# assuming that the user inputs only 4 factors
Q_parameterScalingArray = [0.25, 0.25, 0.25, 0.25]


def Q(quality, persons, Q_parameterArray):
    parameter_X_weight = 0
    for i in range(len(Q_parameterArray)):
        parameter_X_weight += Q_parameterArray[i] * Q_parameterScalingArray[i]
    return parameter_X_weight * quality * persons


Q_basic = 1
Qfunc = lambda value: float(value) * Q_basic


def qualityFactorsInput(qualityScalingFactorsArray):
    global qualityBasic, qualityStandard, qualityHigh, qualityPremium
    qualityBasic, qualityStandard, qualityHigh, qualityPremium \
        = map(Qfunc, qualityScalingFactorsArray)
