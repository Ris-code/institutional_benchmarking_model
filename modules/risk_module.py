def R(risk, R_parameterArray):
    parameter_X_weight = 1
    for i in range(len(R_parameterArray)):
        parameter_X_weight *= R_parameterArray[i]
    return parameter_X_weight * 1000 * risk


R_low = 1
Rfunc = lambda value: float(value) * R_low


def riskFactorsInput(riskScalingFactorsArray):
    global riskLow, riskMedium, riskHigh, riskComplex
    riskLow, riskMedium, riskHigh, riskComplex \
        = map(Rfunc, riskScalingFactorsArray)
