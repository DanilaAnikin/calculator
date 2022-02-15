
class Solver():

    def find_start(self, input, i): # i - index of number last character
        i-=1
        while True:
            char = input[i]
            if(i==0):
                return 0
            elif(char=='+' or char=='-' or char=='*' or char=='/'):
                return(i+1)

            i-=1



    def find_end(self, input, i):
        i+=1
        while True:
            char = input[i]

            if(i==len(input)-1):
                return len(input)-1
            elif(char=='+' or char=='-' or char=='*' or char=='/'):
                return(i-1)

            i+=1





    def solve(self, input):
        result = input
        i = 0
        while "*" in input or "/" in input:
            char = input[i]

            if (char == "*" or char == "/"):
                start = self.find_start(input, i)
                end = self.find_end(input, i)

                num1 = input[start:i]
                num2 = input[i + 1:end + 1]

                result = float(num1)

                if (char == "*"):
                    result *= float(num2)

                elif (char == "/"):
                    result /= float(num2)

                start_string = input[0:(i - len(num1))]  # "0 -> to i-num_len"
                end_string = input[(i + len(num2)) + 1: len(input)]  # "from i+num2_len -> end"

                return self.solve(start_string + str(result) + end_string)
            i += 1

        for char in input:
            if i == 0 and input[i] == '-':
                i+=1
                continue

            if(char == "-" or char=="+"):
                start = self.find_start(input, i)
                end = self.find_end(input, i)

                num1 = input[start:i]
                num2 = input[i+1:end+1]

                result = float(num1)

                if(char == "-"):
                    result -= float(num2)

                elif(char == "+"):
                    result += float(num2)

                start_string = input[0:(i-len(num1))]
                end_string = input[(i+len(num2))+1:len(input)]

                return self.solve(start_string + str(result) + end_string)

            i+=1
        return float(result)

solver = Solver()
