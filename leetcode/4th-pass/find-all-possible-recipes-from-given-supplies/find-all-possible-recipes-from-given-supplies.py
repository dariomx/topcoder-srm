class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        tmp = dict()
        for j in range(len(ingredients)):
            tmp[recipes[j]] = ingredients[j]
        ingredients = tmp
        recipes = set(recipes)
        supplies = set(supplies)
        
        in_stack = {r:False for r in recipes}
        ans = []    
        def rec(r):
            if r in supplies:
                return True
            elif r not in recipes:
                return False
            elif in_stack[r]:
               return False
            else:
                in_stack[r] = True
            for i in ingredients[r]:
                if not rec(i):
                    return False
            ans.append(r)
            supplies.add(r)
            return True
        
        for r in recipes:
            rec(r)
        return ans
        
