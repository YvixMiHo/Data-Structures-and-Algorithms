import unittest
import pytest
from DSA.Data_Structures.Arrays.array_problems import removeDuplicates, removeElements

# nums = [1, 2, 2,1]
# nums2 = [0,0,1,1,1,2,2,3,3,4]
# nums3 = [-2,-1,-1,0,1,2,2]
# nums4 = [-4,-3,-3,-2,-2,-1,-1,0,0]
# nums5 = [0]
# nums6 = []
#
# expectedNums = [1,2,'_']
# expectedNums2 = [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']
# expectedNums3 = [-2,-1,0,1,2, '_','_']
# expectedNums4 = [-4,-3,-2,-1,0,'_', '_', '_', '_', '_']
# expectedNums5 = [0]
# expectedNums6 = []

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



if __name__ == '__main__':
    unittest.main()
