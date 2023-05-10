import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, axis=0):
    try:
        arr1 = np.squeeze(arr1)
        arr2 = np.squeeze(arr2)

        combined_array = np.concatenate((arr1, arr2), axis=axis)

        return combined_array
    except:
        raise ValueError("Combination is not possible")


if __name__ == "__main__":
    # use this for your own testing!

    pass
