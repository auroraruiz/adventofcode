import os
if __name__ == "__main__":
    PATH = os.getcwd()
    FILE = "ex19.txt"
    with open(os.path.join(PATH, FILE), encoding='utf-8') as f:
        wflows, parts  = f.read().split("\n\n")
        wflows = wflows.split("\n")
        parts = parts.split("\n")
        parts = [[int(p.split('=')[-1]) for p in part[:-1].split(',')] for part in parts]

    def process_condition(c):
        if ':' in c:
            c = c.split(':')
            if '<' in c[0]:
                return [0, c[0].split('<'), c[1]]
            elif '>' in c[0]:
                return [1, c[0].split('>'), c[1]]
        return c

    def wflows_dict(wflows, process_function):
        w_dict = {}
        for w in wflows:
            k, v = w.split("{")
            v = v[:-1]
            v = v.split(",")
            w_dict[k] = [process_function(i) for i in v]
        return w_dict
    
    w_dict = wflows_dict(wflows, process_condition)
    print(w_dict)

