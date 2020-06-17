# emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the datalad package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##

import logging
from datalad.api import (
    Dataset,
)
from datalad.utils import Path
from datalad.tests.utils import (
    with_tempfile
)
from datalad_osf.utils import osf_project

common_init_opts = ["encryption=none", "type=external", "externaltype=osf",
                    "autoenable=true"]


@osf_project(title="CI osf-special-remote")
@with_tempfile
def test_gitannex(osf_id, dspath):
    from datalad.cmd import (
        GitRunner,
        WitlessRunner
    )
    dspath = Path(dspath)

    ds = Dataset(dspath).create()

    # add remote parameters here
    init_remote_opts = ["project={}".format(osf_id)]

    import pdb; pdb.set_trace()
    # add special remote
    init_opts = common_init_opts + []
    ds.repo.init_remote('osfproject', options=init_opts)

    # run git-annex-testremote
    # note, that we don't want to capture output. If something goes wrong we
    # want to see it in test build's output log.
    WitlessRunner(
        cwd=dspath,
        env=GitRunner.get_git_environ_adjusted()).run(
            ['git', 'annex', 'testremote', 'osfproject']
    )
