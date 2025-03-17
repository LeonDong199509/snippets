class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # Initial solution, choose the index have highest tank = tank - cost[i] + tank[i+1]
        # result = -1
        # max_tank = 0
        # for i in range(len(gas)):
        #     if gas[i] < cost[i]:
        #         continue
        #     next_index = 0 if i+1 == len(gas) else i+1
        #     start_tank = gas[i] - cost[i] + gas[next_index]
        #     if start_tank > max_tank:
        #         max_tank = start_tank
        #         result = i

        # # Validate the result
        # if result != -1:
        #     i = 0 if result+1 == len(gas) else result+1
        #     tank = gas[result] - cost[result] + gas[i]
        #     while (i != result):
        #         print(tank, i)
        #         next_index = 0 if i+1 == len(gas) else i+1
        #         tank = tank - cost[i] + gas[next_index]
        #         print(next_index, tank, cost[next_index])
        #         if tank < cost[next_index]:
        #             return -1
        #         i = next_index
        
        # return result

        # Greedy solution, Time Complexity O(n), Space Complexity O(1)
    #  • Greedy Property: At each station, the greedy choice is to decide whether to continue from that station or reset and start from the next station. If the fuel balance goes negative at any station, we reset. This greedy choice ensures that we are moving toward a globally optimal solution by eliminating stations that won’t work.
	# •	Optimal Substructure: The solution to the problem can be built by solving smaller subproblems (deciding if starting at each station leads to a valid trip). The overall solution can be obtained by combining the results of these subproblems, and the first valid station found will be the solution.
        cost_sum = sum(cost)
        gas_sum = sum(gas)
        # Check if there is a solution, by comparing the sum of cost and gas
        if gas_sum < cost_sum:
            return -1
        
        # Iterate the List, the index whose following tank will not be below 0 is the answer
        # Why?
        # Of course, the index before it is not the answer, because they are below 0.
        # How about the index after it? 
        # The question makes aure there is only one answer if there is a solution. Because at each index after it, the tank is above 0, which means all index after is are possiable answers. But if any index after it is the answer, the start index will also be an answer, which contradicts the rule that there is onlt one answer. So the start index is always the answer!
        current_tank = 0
        for i in range(len(gas)):
          if current_tank == 0:
              result = i
          current_tank = current_tank + gas[i] - cost[i]
          if current_tank < 0:
              current_tank = 0
        
        return result
        
