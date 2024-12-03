import unittest
from pickle import FALSE

import pytest
from DSA.Data_Structures.Arrays.array_problems import removeDuplicates, removeElements, selfConcatenation
from DSA.Data_Structures.Arrays.stack_problems import isValidParentheses, MinStack


class TestArrayMethods:
    # @pytest.fixture(autouse=True)
    # def setup_method(self, params):
    #     """" Setup for each test method """
    #     self.input_array = params.param.get('input_array')
    #     self.expected_output = params.param.get('expected_output')

    @pytest.mark.parametrize("input_data", [
        {'input_array': [],                    'expected_output': []              },
        {'input_array': [1],                   'expected_output': [1]             },
        {'input_array': [2, 2],                'expected_output': [2]             },
        {'input_array': [1, 2, 2, 1],          'expected_output': [1, 2, 2, 1]    },
        {'input_array': [-2, -1, -1, 0, 1],    'expected_output': [-2, -1, 0, 1]  },
        {'input_array': [0,0,1,1,1,2,2,3,3,4], 'expected_output': [0, 1, 2, 3, 4] },
    ])

    def test_remove_duplicates(self, input_data):
        input_array     = input_data['input_array']
        expected_output = input_data['expected_output']
        result_array = input_array
        k = removeDuplicates(result_array)
        if k <= 0:
            assert result_array[:] == expected_output
        else:
            assert result_array[:k] == expected_output

    @pytest.mark.parametrize("input_data", [
        {'input_array': [],                             'key': 0,  'expected_output': []                    },
        {'input_array': [1],                            'key': 1,  'expected_output': []                    },
        {'input_array': [2, 2],                         'key': 2,  'expected_output': []                    },
        {'input_array': [1, 2, 2, 1],                   'key': 2,  'expected_output': [1, 1]                },
        {'input_array': [-2, -1, -1, 0, 1],             'key': -2, 'expected_output': [-1, -1, 0, 1]        },
        {'input_array': [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 'key': 1,  'expected_output': [0, 0, 2, 2, 3, 3, 4] },
    ])

    def test_remove_elements(self, input_data):
            input_array     = input_data['input_array']
            expected_output = input_data['expected_output']
            key             = input_data['key']
            k = removeElements(input_array,key)
            input_array[:k] = sorted(input_array[:k])
            assert input_array[:k] == expected_output


    @pytest.mark.parametrize("input_data", [
        {'input_array': [],         'expected_output': []                    },
        {'input_array': [1],        'expected_output': [1,1]                 },
        {'input_array': [1, 2, 3],  'expected_output': [1,2,3,1,2,3]       },
    ])

    def test_self_concatenation(self, input_data):
            input_array     = input_data['input_array']
            expected_output = input_data['expected_output']
            output_array = selfConcatenation(input_array)
            assert output_array == expected_output

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

    # @pytest.mark.parametrize("operations, expected_outputs", [
    #     (
    #         ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
    #         [None, None, None, None, -3, None, 0, -2]
    #     )
    # ])
    #
    # def test_MinStack(self,operations, expected_outputs):
    #         Stack = MinStack()
    #         values = [-2, 0, -3]
    #         output = []
    #         val_idx = 0
    #
    #         print(f"Output initial: {output}")
    #
    #         for _,operation in enumerate(operations):
    #             match operation:
    #                     case "MinStack":
    #                         output.append(None)
    #                     case "push":
    #                         if val_idx < len(values):
    #                             Stack.push(values[val_idx])
    #                             val_idx+=1
    #                         output.append(None)
    #                     case "pop":
    #                         output.append(Stack.pop())
    #                     case "top":
    #                         output.append(Stack.top())
    #                     case "getMin":
    #                         output.append(Stack.getMin())
    #                     case _:
    #                         assert False, f"Unexpected operation: {operation}"
    #
    #         print(f"Output final: {output}")
    #         print(f"Expected Outputs: {expected_outputs}")
    #         assert output == expected_outputs, f"Test failed! Output: {output}, Expected: {expected_outputs}"
    #         assert len(output) == len(expected_outputs), f"Length mismatch! Output length: {len(output)}, Expected length: {len(expected_outputs)}"

if __name__ == '__main__':
    unittest.main()
