from os.path import join, dirname, islink, exists, expanduser, realpath
import os, re
import mx

# Verify symlinks to JDK sources and tests
suite_dir = dirname(__file__)
top_dir = dirname(suite_dir)
src_link = join(top_dir, 'src')
if not islink(src_link):
    if exists(src_link):
        mx.abort('{} exists but is not a symlink - please remove it'.format(src_link))
    openjdk_src = expanduser('~/jdk-jdk/open/src')
    if exists(openjdk_src):
        os.symlink(openjdk_src, src_link)
    else:
        mx.abort('Link to JDK/src directory does not exist ({}). Please create it'.format(src_link))
openjdk_dir = dirname(realpath(src_link))
test_link = join(top_dir, 'test')
if not islink(test_link):
    if exists(test_link):
        mx.abort('{} exists but is not a symlink - please remove it'.format(test_link))
    os.symlink(join(openjdk_dir, 'test'), test_link)

# Set up chekstyle config
checkstyle_conf = join(top_dir, 'checkstyle_checks.xml')
assert exists(checkstyle_conf)
checkstyle_conf_dst = join(openjdk_dir, 'src/jdk.internal.vm.ci/share/classes/jdk.vm.ci.services/.checkstyle_checks.xml')
if not exists(checkstyle_conf_dst) or realpath(checkstyle_conf_dst) != checkstyle_conf:
    os.symlink(checkstyle_conf, checkstyle_conf_dst)

# Patch top level .gitignore
my_gitignore_path = join(top_dir, '.gitignore')
gitignore_path = join(openjdk_dir, '.gitignore')
with open(gitignore_path) as fp:
    gitignore = fp.read()
with open(my_gitignore_path) as fp:
    my_gitignore = fp.read()
start = '# -- BEGIN mx_jdk GENERATED' + os.linesep
end = '# -- END mx_jdk GENERATED' + os.linesep
gitignore = re.sub(start + '.*' + end, '', gitignore, flags=re.DOTALL) + start + my_gitignore + end
with open(gitignore_path, 'w') as fp:
    fp.write(gitignore)
