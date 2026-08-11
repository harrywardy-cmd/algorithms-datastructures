class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Use a set to store unique email addresses
        unique = set()

        # Process each email address
        for i in emails:

            # Split the email into the local part and domain
            local, domain = i.split('@')

            # Ignore everything after '+' in the local part
            local = local.split("+")[0]

            # Remove all '.' characters from the local part
            local = local.replace(".", "")

            # Add the normalized email as a tuple to the set
            unique.add((local, domain))

        # Return the number of unique normalized email addresses
        return len(unique)
