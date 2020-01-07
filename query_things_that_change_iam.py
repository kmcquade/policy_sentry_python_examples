from policy_sentry.shared.database import connect_db
from policy_sentry.querying.actions import get_actions_with_access_level


def query_for_changing_iam_things(db_session):
    actions_that_change_iam = []
    iam_permissions_management_actions = get_actions_with_access_level(db_session, 'iam', 'Permissions management')
    iam_write_actions = get_actions_with_access_level(db_session, 'iam', 'Write')
    actions_that_change_iam.extend(iam_permissions_management_actions)
    actions_that_change_iam.extend(iam_write_actions)
    return actions_that_change_iam


if __name__ == '__main__':
    db_session = connect_db('bundled')
    actions_that_change_iam = query_for_changing_iam_things(db_session)
    print("Actions that change IAM")
    for action in actions_that_change_iam:
        print(action)
