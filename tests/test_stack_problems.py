import unittest
import pytest
from DSA.Data_Structures.Arrays.stack_problems import isValidParentheses, MinStack

class TestStackMethods:
    # @pytest.fixture(autouse=True)
    # def setup_method(self, params):
    #     """" Setup for each test method """
    #     self.input_array = params.param.get('input_array')
    #     self.expected_output = params.param.get('expected_output')


    @pytest.mark.parametrize("input_data", [
        {'input_array':  "",            'expected_output': False    },
        {'input_array':  "[",           'expected_output': False    },
        {'input_array':  "](",          'expected_output': False    },
        {'input_array':  "[]",          'expected_output': True     },
        {'input_array':  "[(])",        'expected_output': False    },
        {'input_array':  "([{}])",      'expected_output': True     },
        {'input_array':  "()[]{}",      'expected_output': True     },
    ])

    def test_is_valid_parentheses(self, input_data):
            input_array     = input_data['input_array']
            expected_output = input_data['expected_output']
            status = isValidParentheses(input_array)
            assert status == expected_output

    @pytest.mark.parametrize("operations, expected_outputs", [
        (
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [None, None, None, None, -3, None, 0, -2]
        )
    ])

    def test_MinStack(self,operations, expected_outputs):
            Stack = MinStack()
            values = [-2, 0, -3]
            output = []
            val_idx = 0

            for operation in operations:
                match operation:
                        case "MinStack":
                            output.append(None)
                        case "push":
                            if val_idx < len(values):
                                Stack.push(values[val_idx])
                                val_idx+=1
                            output.append(None)
                        case "pop":
                            output.append(Stack.pop())
                        case "top":
                            output.append(Stack.top())
                        case "getMin":
                            output.append(Stack.getMin())
                        case _:
                            assert False, f"Unexpected operation: {operation}"

            assert len(output) == len(expected_outputs), f"Length mismatch! Output length: {len(output)}, Expected length: {len(expected_outputs)}"
            assert output == expected_outputs, f"Test failed! Output: {output}, Expected: {expected_outputs}"


if __name__ == '__main__':
    unittest.main()
