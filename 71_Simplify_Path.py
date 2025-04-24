class Solution:
    def simplifyPath(self, path: str) -> str:
        sub_dirs = path.split('/')
        result_list = []

        for sub_dir in sub_dirs:
            if not sub_dir or sub_dir == ".":
                continue

            if sub_dir == "..":
                if result_list:
                    result_list.pop()
            else:
                result_list.append(sub_dir)
        
        result = '/'.join(result_list)
  
        
        return '/' + result

