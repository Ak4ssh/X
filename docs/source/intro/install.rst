Install Guide
=============

Being a modern Python framework, X requires an up to date version of Python to be installed in your system.
We recommend using the latest versions of both Python 3 and pip.

.. contents:: Contents
    :backlinks: none
    :depth: 1
    :local:

-----

Install X
----------------

-   The easiest way to install and upgrade X to its latest stable version is by using **pip**:

    .. code-block:: text

        $ pip3 install -U X

-   or, with :doc:`TgCrypto <../topics/speedups>` as extra requirement (recommended):

    .. code-block:: text

        $ pip3 install -U X tgcrypto

Bleeding Edge
-------------

You can install the development version from the git ``master`` branch using this command:

.. code-block:: text

    $ pip3 install -U https://github.com/X/X/archive/master.zip

Verifying
---------

To verify that X is correctly installed, open a Python shell and import it.
If no error shows up you are good to go.

.. parsed-literal::

    >>> import X
    >>> X.__version__
    'x.y.z'

.. _`Github repo`: http://github.com/X/X
