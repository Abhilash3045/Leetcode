class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        i = 0
        new = ""
        while i < len(command):
            if command[i]==")":
                pass
            elif command[i]!="(":
                new+=command[i]
            elif command[i]+command[i+1]=="()":
                new+="o"
                i += 1
            i += 1
        return new