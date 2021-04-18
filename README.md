This repository defines an [mx suite](https://github.com/graalvm/mx#suites) that
can be used to generate configuration files necessary for editing the JVMCI Java
and C++ sources in [OpenJDK](https://github.com/openjdk/jdk) using Eclipse.

## Getting Started

1. Clone mx and put it on your PATH:
```
git clone https://github.com/graalvm/mx $HOME/mx
export PATH=$PATH:$HOME/mx
```
2. Set JAVA_HOME to point to a [boot JDK](https://github.com/openjdk/jdk/blob/master/doc/building.md#boot-jdk-requirements):
```
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-16.jdk/Contents/Home
```
3. Create a symlink to the `src` top level directory in the OpenJDK repo.
   If it is in `~/jdk-jdk/open` you can skip this step as it will be done automatically.
4. Generate the Eclipse configuration:
```
mx eclipseinit
```
5. Open the generated Eclipse projects in Eclipse: `File` -> `Import` -> `Git` -> `Projects from Git` -> _select local copy of this repo_ -> `Next` -> `Finish`
