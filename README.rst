========================
python-ldap_paged_search
========================

Summary
=======

ldap_paged_search is a python library to easily perform LDAP queries with more
than 1000 results, or to break down queries into smaller result sets.

Many LDAP servers will not allow queries with over 1000 results unless the
queries are paged.  The existing python ldap library does support pageing, but
requires some not very intuitive coding to perform it.  This library is simply a
wrapper for that code.

Its interface is also slightly easier to perform queries than the LDAP library
it wraps.

Requirements
============

* Tested on python 2.8
* Default python library includes ldap library

Installation
============

Via pip or easy_install::

    $ sudo pip install ldap_paged_search   # If you prefer PIP
    $ sudo easy_install ldap_paged_search  # If you prefer easy_install

Manual installation::

    $ git clone https://github.com/neoCrimeLabs/python-ldap_paged_search.git
    $ cd python-ldap_paged_search
    $ sudo python setup.py install

Usage
=====

Initial setup

.. code:: python

    from ldappagedsearch import LdapPagedSearch

    # Required values
    url             = 'ldap://your.ldap.server'
    username        = 'username'      # for anything but active directory
    username        = 'domain\\user'  # for active directory
    password        = 'yourPassword'

    baseDN          = 'dc=company,dc=com'
    searchFilter    = '(&(objectCategory=user))'

    # Optional values
    maxPages        = 0     # 0 = everything
    pageSize        = 1000  # How many records per page
                            # Usual max is 1000; check your LDAP server docs

Defining a callback method::

    # Using a callback method to process results uses less memory on large queries
    # Not using a callback search() will return all results as a single list

    def myCallback(dn,record):
        print dn, record

Query using 'with'::

    with LdapPagedSearch(url, username, password, maxPages=2, pageSize=2 ) as l:
        results = l.search(baseDN, searchFilter, callback = myCallback)

        # maxPages, pageSize, and callback are all OPTIONAL

Another way t0o query::

    l = LdapPagedSearch(url, username, password, maxPages=2, pageSize=2 )
    results = l.search(baseDN, searchFilter, callback = myCallback)
    
    # maxPages, pageSize, and callback are all OPTIONAL

Results format::

    # If you don't set a callback, your results will be returned as follows

    [
        ('DistinctName1',
            {
                'FieldName':    ['value1', 'value2'],
                'AnotherField': ['value'], }),
        ('DistinctName2',
            {
                'FieldName':    ['value1', 'value2'],
                'AnotherField': ['value'], }),
        ...
    ]

    
