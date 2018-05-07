#First question To flatten the nested list
import types
def flatten_list(nested_list):
    """
    Flatten a arbitrarily nested list
    Args:
    nested_list: a nested list with item to be either integer or list
    example:
      [2,[[3,[4]], 5]]
    Returns:
    a flattened list with only integers
    example:
      [2,3,4,5]
    """
    result=[]
    if isinstance(nested_list,int):
        result.append(nested_list)
        return result
    for a in nested_list:
        tmp=flatten_list(a)
        result+=tmp
    return result
if __name__=='__main__':
    print flatten_list([1,2,[3,4,[5]]])
