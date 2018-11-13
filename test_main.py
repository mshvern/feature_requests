from unittest import TestCase, mock

from . import app
from .database.models import FeatureRequest


class MainTest(TestCase):

    def setUp(self):
        self.filler = {
            "description": None,
            "title": None,
            "product_area_id": None,
            "client_id": None,
            "target_date": None
        }
        self.mock_feature_requests = [
            FeatureRequest(client_priority=1, **self.filler),
            FeatureRequest(client_priority=2, **self.filler)
        ]

    @mock.patch("feature_requests.app.db_session")
    def test_resort_client_priorities(self, mock_session: mock.Mock):
        with mock.patch("feature_requests.app.get_all_feature_requests_by_client_id",
                        return_value=self.mock_feature_requests) as mock_query:

            # Test if we can insert a feature request in the front in terms of client priority
            # And also test if db_session was called to save the instances
            ret = app.resort_feature_requests(1, 2)
            self.assertEqual(ret, 1)
            self.mock_feature_requests.insert(ret-1, FeatureRequest(client_priority=ret, **self.filler))
            mock_query.called_once()
            mock_session.commit.assert_called_once()
            mock_session.bulk_save_objects.assert_called_once()

            ret = app.resort_feature_requests(5, 2)
            self.assertEqual(ret, 4)
            self.mock_feature_requests.insert(ret-1, FeatureRequest(client_priority=ret, **self.filler))

            # Test if we can insert a feature request in the middle
            ret = app.resort_feature_requests(2, 2)
            self.assertEqual(ret, 2)
            self.mock_feature_requests.insert(ret-1, FeatureRequest(client_priority=ret, **self.filler))

            # Test for consistency
            self.assertListEqual(
                [feature_request.client_priority for feature_request in self.mock_feature_requests],
                [1, 2, 3, 4, 5]
            )
