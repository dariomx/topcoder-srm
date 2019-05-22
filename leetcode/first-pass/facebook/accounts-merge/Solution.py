from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts):
        email_users = defaultdict(list)
        n = len(accounts)
        for user_id in range(n):
            for i in range(1, len(accounts[user_id])):
                email = accounts[user_id][i]
                email_users[email].append(user_id)

        def dfs(start, visited):
            stack = [start]
            emails = set()
            while stack:
                user_id = stack.pop()
                if user_id in visited:
                    continue
                visited.add(user_id)
                for i in range(1, len(accounts[user_id])):
                    email = accounts[user_id][i]
                    emails.add(email)
                    stack += email_users[email]
            return [accounts[start][0]] + sorted(emails)

        visited = set()
        ans = []
        for user_id in range(n):
            if user_id not in visited:
                ans.append(dfs(user_id, visited))
        return ans
