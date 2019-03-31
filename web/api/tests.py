# https://github.com/beda-software/drf-writable-nested/blob/master/tests/test_writable_nested_model_serializer.py

from rest_framework.test import APITestCase


def get_initial_data():
    return {
        'name': 'group2',
        'is_display': True,
        'codes': [
            {
                'code': 'code2',
                'translations': [
                    {
                        'translation': 'テスト'
                    }
                ]
            }
        ]
    }


class MyTest(APITestCase):

    def test_create(self):

        data = get_initial_data()
        # result = self.client.put('/api/code_groups/bulk/1', data=data, format='json')
        result = self.client.options('/api/code_groups')
        result = self.client.put('/api/code_groups', data=data, format='json')
        self.assertEqual(201, result.status_code)
        print(result.data)

        # # 取得できるか確認
        # result = self.client.get('/api/code_group/1', data=data, format='json')
        # self.assertEqual(200, result.status_code)
        #
        # # 更新
        # print(result.data)
        # result = self.client.put('/api/code_group/', data=result.data, format='json')
        # self.assertEqual(200, result.status_code)
        # print(result.data)
