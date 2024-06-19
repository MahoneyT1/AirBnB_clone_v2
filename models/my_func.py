



def single_double_quote(str, key):
        """ a function that strips a string leading and trailing quotes
        sing quotes or double quotes
        args:
            (str) string to strip quotes
            (key) key to create new dict with
        """ 
        obj_to_return = {}       
                
        if str.startswith('"') or str.startswith("'")\
            and str.endswith('"') or str.endswith("'"):
            striped_values =  str.strip('"').strip("'")
            obj_to_return[key] = striped_values
        else:
            obj_to_return[key] = str
        return obj_to_return

if __name__ == "__main__":
    single_double_quote()