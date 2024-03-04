def floatcategorizer(float_value):
    if 0.00 <= float(float_value) < 0.07:
        if 0.00 <= float(float_value) < 0.01:
            min_float = 0.00
            max_float = 0.01
            return min_float,max_float
        if 0.01 <= float(float_value) < 0.02:
            min_float = 0.01
            max_float = 0.02
            return min_float,max_float
        if 0.02 <= float(float_value) < 0.03:
            min_float = 0.02
            max_float = 0.03
            return min_float,max_float
        if 0.03 <= float(float_value) < 0.04:
            min_float = 0.03
            max_float = 0.04
            return min_float,max_float
        if 0.04 <= float(float_value) < 0.07:
            min_float = 0.04
            max_float = 0.07
            return min_float,max_float

    elif 0.07 <= float(float_value) < 0.15:
        if 0.07 <= float(float_value) < 0.08:
            min_float = 0.07
            max_float = 0.08
            return min_float, max_float
        if 0.08 <= float(float_value) < 0.09:
            min_float = 0.08
            max_float = 0.09
            return min_float, max_float
        if 0.09 <= float(float_value) < 0.10:
            min_float = 0.09
            max_float = 0.10
            return min_float, max_float
        if 0.10 <= float(float_value) < 0.11:
            min_float = 0.10
            max_float = 0.11
            return min_float, max_float
        if 0.11 <= float(float_value) < 0.15:
            min_float = 0.11
            max_float = 0.15
            return min_float, max_float

    elif 0.15 <= float(float_value) < 0.38:
        if 0.15 <= float(float_value) < 0.18:
            min_float = 0.15
            max_float = 0.18
            return min_float, max_float
        if 0.18 <= float(float_value) < 0.21:
            min_float = 0.18
            max_float = 0.21
            return min_float, max_float
        if 0.21 <= float(float_value) < 0.24:
            min_float = 0.21
            max_float = 0.24
            return min_float, max_float
        if 0.24 <= float(float_value) < 0.27:
            min_float = 0.24
            max_float = 0.27
            return min_float, max_float
        if 0.27 <= float(float_value) < 0.38:
            min_float = 0.27
            max_float = 0.38
            return min_float, max_float

    elif 0.38 <= float(float_value) < 0.45:
        if 0.38 <= float(float_value) < 0.39:
            min_float = 0.38
            max_float = 0.39
            return min_float, max_float
        if 0.39 <= float(float_value) < 0.40:
            min_float = 0.39
            max_float = 0.40
            return min_float, max_float
        if 0.40 <= float(float_value) < 0.41:
            min_float = 0.40
            max_float = 0.41
            return min_float, max_float
        if 0.41 <= float(float_value) < 0.42:
            min_float = 0.41
            max_float = 0.42
            return min_float, max_float
        if 0.42 <= float(float_value) < 0.45:
            min_float = 0.42
            max_float = 0.45
            return min_float, max_float

    elif 0.45 <= float(float_value) <= 1.00:
        if 0.45 <= float(float_value) < 0.50:
            min_float = 0.45
            max_float = 0.50
            return min_float, max_float
        if 0.50 <= float(float_value) < 0.63:
            min_float = 0.50
            max_float = 0.63
            return min_float, max_float
        if 0.63 <= float(float_value) < 0.76:
            min_float = 0.63
            max_float = 0.76
            return min_float, max_float
        if 0.76 <= float(float_value) < 0.90:
            min_float = 0.76
            max_float = 0.90
            return min_float, max_float
        if 0.90 <= float(float_value) < 1.00:
            min_float = 0.90
            max_float = 1.00
            return min_float, max_float

    else:
        return "Invalid Condition"  # Handle values outside the specified ranges



#if __name__ == '__main__':
#    result = floatcategorizer("0.15")
#    min_float, max_float = result
#    print(f"The item is in condition: {min_float} - {max_float}")