import fnmatch
from os.path import isdir, join

def include_patterns(*patterns):

    def _ignore_patterns(path, all_names):
        keep = (name for pattern in patterns
                        for name in fnmatch.filter(all_names, pattern))
        dir_names = (name for name in all_names if isdir(join(path, name)))
        return set(all_names) - set(keep) - set(dir_names)

    return _ignore_patterns


if __name__ == '__main__':

    from shutil import copytree, rmtree
    import os

    src = r'/path/to/source'
    dst = r'/path/to/destination/'

    if os.path.exists(dst) and os.path.isdir(dst):
        print('removing existing directory "{}"'.format(dst))
        rmtree(dst, ignore_errors=False)

    copytree(src, dst, ignore=include_patterns("*00010001*.*"))

    print('done')
