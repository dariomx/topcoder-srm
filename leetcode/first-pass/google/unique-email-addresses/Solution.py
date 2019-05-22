class Solution:
    def numUniqueEmails(self, emails):
        uniq = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".","")
            uniq.add(local + "@" + domain)
        return len(uniq)