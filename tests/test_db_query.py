from src.managers import BaseManager


class TestDbQueryFetch(BaseManager):
    _FETCH_QUERY = '''select * from contacts order by first_name'''

    @property
    def fetch(self):
        data = super().fetch()
        return data


class TestDBQueryCommit(BaseManager):

    _FETCH_QUERY = (
        # '''update contacts set first_name=%s, last_name=%s, email=%s where id=%s'''
        # '''insert into contacts (first_name, last_name, email) values(%s, %s, %s)'''
        """
    insert into contacts (id, first_name, last_name, email) values(%s, %s, %s, %s)
    on conflict (id) do 
    update set first_name=EXCLUDED.first_name, last_name=EXCLUDED.last_name, email=EXCLUDED.email
    """

    )

    def commit(self, *args):
        return super().commit(*args)


if __name__ == "__main__":
    test_data = TestDbQueryFetch()

    data = test_data.fetch
    # print(data, len(data))
    assert data is not False, "There is no data, check settings"

    # test_update = TestDBQueryCommit()

    # test_update.commit("Steeve123", "Jopas257", "mystylenamebndf@gmail.com", 1)


    # test_insert = TestDBQueryCommit()

    # test_insert.commit(13, "Steeve1133", "Jopas257", "hotgachimanniciest@gmail.com")
