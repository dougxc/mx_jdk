suite = {
    "mxversion" : "5.292.0",
    "name" : "jdk",

    # ------------- Libraries -------------

    "libraries" : {

        "TESTNG" : {
            "sha1" : "6feb3e964aeb7097aff30c372aac3ec0f8d87ede",
            "maven" : {
                "groupId" : "org.testng",
                "artifactId" : "testng",
                "version" : "6.9.10",
            },
        },
    },

    "projects" : {

        # ------------- JVMCI:Service -------------

        "jdk.vm.ci.services" : {
            "subDir" : "src/jdk.internal.vm.ci/share/classes",
            "sourceDirs" : ["src"],
            "requiresConcealed" : {
                "java.base" : [
                    "jdk.internal.misc"
                ],
            },
            "javaCompliance" : "16+",
            "checkstyleVersion" : "8.36.1",
        },

        # ------------- JVMCI:API -------------

        "jdk.vm.ci.common" : {
            "subDir" : "src/jdk.internal.vm.ci/share/classes",
            "sourceDirs" : ["src"],
            "dependencies" : [
              "jdk.vm.ci.services",
            ],
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },

        "jdk.vm.ci.meta" : {
            "subDir" : "src/jdk.internal.vm.ci/share/classes",
            "sourceDirs" : ["src"],
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },

        "jdk.vm.ci.code" : {
            "subDir" : "src/jdk.internal.vm.ci/share/classes",
            "sourceDirs" : ["src"],
            "dependencies" : ["jdk.vm.ci.meta", "jdk.vm.ci.common"],
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },

        "jdk.vm.ci.code.test" : {
            "subDir" : "test/hotspot/jtreg/compiler/jvmci",
            "sourceDirs" : ["src"],
            "dependencies" : [
                "mx:JUNIT",
                "jdk.vm.ci.aarch64",
                "jdk.vm.ci.amd64",
                "jdk.vm.ci.code",
                "jdk.vm.ci.hotspot",
            ],
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },

        "jdk.vm.ci.runtime" : {
            "subDir" : "src/jdk.internal.vm.ci/share/classes",
            "sourceDirs" : ["src"],
            "dependencies" : [
                "jdk.vm.ci.code",
            ],
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },

        "jdk.vm.ci.runtime.test" : {
            "subDir" : "test/hotspot/jtreg/compiler/jvmci",
            "sourceDirs" : ["src"],
            "requiresConcealed" : {
                "java.base" : [
                    "jdk.internal.reflect",
                    "jdk.internal.misc",
                    "jdk.internal.org.objectweb.asm"
                ],
            },
            "dependencies" : [
                "mx:JUNIT",
                "TESTNG",
                "jdk.vm.ci.common",
                "jdk.vm.ci.runtime",
            ],
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },

        # ------------- JVMCI:HotSpot -------------

        "jdk.vm.ci.aarch64" : {
            "subDir" : "src/jdk.internal.vm.ci/share/classes",
            "sourceDirs" : ["src"],
            "dependencies" : ["jdk.vm.ci.code"],
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },

        "jdk.vm.ci.amd64" : {
            "subDir" : "src/jdk.internal.vm.ci/share/classes",
            "sourceDirs" : ["src"],
            "dependencies" : ["jdk.vm.ci.code"],
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },

        "jdk.vm.ci.hotspot" : {
            "subDir" : "src/jdk.internal.vm.ci/share/classes",
            "sourceDirs" : ["src"],
            "dependencies" : [
                "jdk.vm.ci.runtime",
            ],
            "requiresConcealed" : {
                "java.base" : [
                    "jdk.internal.misc",
                    "jdk.internal.org.objectweb.asm",
                ]
            },
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },

        "jdk.vm.ci.hotspot.test" : {
            "subDir" : "test/hotspot/jtreg/compiler/jvmci",
            "sourceDirs" : ["src"],
            "requiresConcealed" : {
                "java.base" : [
                    "jdk.internal.misc",
                    "jdk.internal.vm.annotation"
                ],
            },
            "dependencies" : [
                "mx:JUNIT",
                "TESTNG",
                "jdk.vm.ci.code.test",
                "jdk.vm.ci.hotspot",
            ],
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },

        "jdk.vm.ci.hotspot.aarch64" : {
            "subDir" : "src/jdk.internal.vm.ci/share/classes",
            "sourceDirs" : ["src"],
            "dependencies" : [
                "jdk.vm.ci.aarch64",
                "jdk.vm.ci.hotspot",
            ],
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },

        "jdk.vm.ci.hotspot.amd64" : {
            "subDir" : "src/jdk.internal.vm.ci/share/classes",
            "sourceDirs" : ["src"],
            "dependencies" : [
                "jdk.vm.ci.amd64",
                "jdk.vm.ci.hotspot",
            ],
            "checkstyle" : "jdk.vm.ci.services",
            "javaCompliance" : "16+",
        },
    },
    "distributions": {
        "JVMCI" : {
            # This distribution defines a module.
            "moduleInfo" : {
                "name" : "jdk.internal.vm.ci",
            },
            "subDir" : "src/jdk.internal.vm.ci/share/classes",
            "dependencies" : [
                "jdk.vm.ci.aarch64",
                "jdk.vm.ci.amd64",
                "jdk.vm.ci.code",
                "jdk.vm.ci.code.test",
                "jdk.vm.ci.common",
                "jdk.vm.ci.hotspot",
                "jdk.vm.ci.hotspot.aarch64",
                "jdk.vm.ci.hotspot.amd64",
                "jdk.vm.ci.hotspot.test",
                "jdk.vm.ci.meta",
                "jdk.vm.ci.runtime",
                "jdk.vm.ci.runtime.test",
                "jdk.vm.ci.services",
            ],
        }
    }
}