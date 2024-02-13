suite = {
  "name" : "mx",
  "libraries" : {

    # ------------- Libraries -------------
    "JACOCOCORE_0.8.10": {
      "digest": "sha512:2bb06291c3717512326ad9a3cacbd29e8a057c3d2555195c82104b3f56e820effbc0870238ea891c231eaf34abb01e9b53ada02055de1736f28aceca077ac89e",
      "sourceDigest": "sha512:1460c272ca2512dd733232daaa1e20488ca9cb5e686261cd0449213da0a2f21b661d8b044b2b3a32a4c07ea5666a9fc653cbaf8e42aed931a6034c57de217458",
      "maven": {
        "groupId": "org.jacoco",
        "artifactId": "org.jacoco.core",
        "version": "0.8.10",
      },
      "dependencies" : ["ASM_9.5", "ASM_COMMONS_9.5", "ASM_TREE_9.5"],
      "license": "EPL-2.0",
    },

    "JACOCOAGENT_0.8.10": {
      "digest": "sha512:67a50cd123be71b3f0f46f4bd94d4d6f9ffa34d08e95cfd3e497f418f71cd8124802007707fab4cae0991b509f63ab4048dfeaa73343bc966fc6091bfdccc680",
      "maven": {
        "groupId": "org.jacoco",
        "artifactId": "org.jacoco.agent",
        "version": "0.8.10",
        "classifier": "runtime",
      },
      "license": "EPL-2.0",
    },

    "JACOCOREPORT_0.8.10": {
      "digest": "sha512:5973d71309c2f45529a84c7e5bf105d80f5df4d9f2cbc95006eb348cf9c5224781c34a8d564718190427913c258dd9d68ac1cd0df0715d02c617bdf95e466e3f",
      "sourceDigest": "sha512:7a884c4aa87a20b0aa218b3a07ecb5a1a69bb38701237a0b89f61f03328361ed2d45069d5ec3f3e13a3db0d831bd35c89a34c9c01ed28e25cac79f072d29eca7",
      "maven": {
        "groupId": "org.jacoco",
        "artifactId": "org.jacoco.report",
        "version": "0.8.10",
      },
      "dependencies" : ["JACOCOCORE_0.8.10"],
      "license": "EPL-2.0",
    },

    "ASM_9.5": {
      "digest": "sha512:9e65f2983783725bae196ca939b45246958731246df1c495089c8ea5ce646de77c4e01a5a9ba10642016bb3258e1727e9ebcece6e74d9e3c32f528025d76b955",
      "sourceDigest": "sha512:64262b68c1acd473a49be3c8a89190200be66808034c55fb23ed08d8a977111c234b6dc77b6ca95310e1f1cbc43437cdc863aadb6217976cc1720d63ef01e937",
      "maven": {
        "groupId": "org.ow2.asm",
        "artifactId": "asm",
        "version": "9.5",
      },
      "license": "BSD-new",
    },

    "ASM_ANALYSIS_9.5": {
      "digest": "sha512:30f1300588a0464110d7a40b07501863626ca8a9085f8ee33686f20ddc5d67e7456fd30168d7168f189142027eb6bcc1a4b9990d24e8ebeada9207ac015e2b46",
      "sourceDigest": "sha512:bfcca1059a2fc5dae998615e006dda282a86a6e6a12bb43955816620642770c2cf5b1bc8d619cb4e7c3d1920a06cec2b51386571b92f3bf5025e2da0d1236822",
      "maven": {
        "groupId": "org.ow2.asm",
        "artifactId": "asm-analysis",
        "version": "9.5",
      },
      "dependencies" : ["ASM_TREE_9.5"],
      "license": "BSD-new",
    },

    "ASM_COMMONS_9.5": {
      "digest": "sha512:6121a9d033627a33839d9bd264fce4a531b6a3f974720adc6150816f0316d1522c3d8caf7df039fdd46cb66bedd788e50f709d4a1f75d3525912ad7a4d87f7da",
      "sourceDigest": "sha512:688d56a1b4fb6f7d86b79b7493a848851892910d00067a0c5effdaf7132266ec7a1ba57a8248c2fd6c0ebdef18a4918908a36e85f5927b9acb55448047a1e333",
      "maven": {
        "groupId": "org.ow2.asm",
        "artifactId": "asm-commons",
        "version": "9.5",
      },
      "dependencies" : ["ASM_9.5", "ASM_TREE_9.5", "ASM_ANALYSIS_9.5"],
      "license": "BSD-new",
    },

    "ASM_TREE_9.5": {
      "digest": "sha512:816de8f84c216a7bd97b2458bde64a4b99a039b7b59fbd1ef52edf8bf869edabb93967736fe0c61e8eb3e1520e0cefe69ba59cda12df30f9f85db75fb6c064f3",
      "sourceDigest": "sha512:a107043c05398091e3f3c614270c626be8ea5a1a547e30dc5709ef92069c8c8baa315c385a68f244c3a37bc148c3aeeec26adc8c00afc2a03a1d21a40e076a4c",
      "maven": {
        "groupId": "org.ow2.asm",
        "artifactId": "asm-tree",
        "version": "9.5",
      },
      "dependencies" : ["ASM_9.5"],
      "license": "BSD-new",
    },

    "SPOTBUGS_3.0.0" : {
      # original: https://sourceforge.net/projects/findbugs/files/findbugs/3.0.0/findbugs-3.0.0.zip/download
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/findbugs-3.0.0.zip"],
      "digest": "sha512:948200dde19ac54a9f353cdae6d584b77f5ed926a4d664b132d5fdfde4f608a8599e798a9f83c41ebba0429876c22cde79de0a00cbe357f4a56fcdb61aba43c1",
    },

    "SPOTBUGS_3.1.11" : {
      # original: https://repo.maven.apache.org/maven2/com/github/spotbugs/spotbugs/3.1.11/spotbugs-3.1.11.zip
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/spotbugs-3.1.11.zip"],
      "digest": "sha512:98572754ab2df4ebc604d286fb8d83a7a053827d522df933cda3bc51f55f22a4123dad34a92954fdcaa3a81bd41dd466fa7ac1c7e4de980101fecef9905763a9",
    },

    "SPOTBUGS_4.4.2" : {
      "urls" : ["https://github.com/spotbugs/spotbugs/releases/download/4.4.2/spotbugs-4.4.2.zip"],
      "digest": "sha512:8ef2b502e684943d317d8f51ab4103c6b0cc716d1b53adf51a43a3cfd34bfd224924dddafa326b760acd6cf630afaf82107bf045cddb8a603f8d55cc4409aab6",
    },

    "SPOTBUGS_4.7.1" : {
      "urls" : ["https://github.com/spotbugs/spotbugs/releases/download/4.7.1/spotbugs-4.7.1.zip"],
      "digest": "sha512:2b19837ed5ef55654139a86579ea3ab8edeaf716245eb61503c0c861038bc32d84d50d7316442f32338aef3688119b9137df28d8d3cea1fb8d0653710d96259d",
    },

    "SPOTBUGS_4.7.3" : {
      "urls" : ["https://github.com/spotbugs/spotbugs/releases/download/4.7.3/spotbugs-4.7.3.zip"],
      "digest": "sha512:fcece0ecbc5301b5d101668b997beda59f4590f01010a6d195e4212ba989150a85760c25bd252966cde82844a43f4992d32bf6fc175ad01d0a578ca573e22c2e",
    },

    "SPOTBUGS_4.7.3_JDK21_BACKPORT" : {
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/spotbugs-4.7.3-jdk21-backport.zip"],
      "digest": "sha512:c8f7ba8154ec40d33d2864b4fdd0c5763a1d6d8f64bb5e2d3204d841e28189d8ef6fe4a6866a72465df607318e3ad9c5d18db7f96cccc502957fd6e2dd6f0537",
    },

    "SIGTEST_1_2" : {
      "maven": {
        "groupId": "org.netbeans.tools",
        "artifactId": "sigtest-maven-plugin",
        "version": "1.2",
      },
      "digest": "sha512:a005b7ec0eb37a34539e5694a2620b4b5acb54104fb04b04aa8321bb63f93fbac985dc131f207b0cc4f94ea8f8b144059991a14ca0b36a46a8bd2b8226c601ef",
    },

    "SIGTEST_1_3" : {
      "maven": {
        "groupId": "org.netbeans.tools",
        "artifactId": "sigtest-maven-plugin",
        "version": "1.3",
      },
      "digest": "sha512:4365f4bbfeca6f61c4d27f89c5bb6aa2fcc88dab3eab4e26a97ddbc6cfc6c2a0a67949b9e3417e43851fb92e04e639b7eb19c8c00c91ddfca9f1a6df4ec7deef",
    },

    "CODESNIPPET-DOCLET_1.0" : {
      "maven" : {
        "groupId" : "org.apidesign.javadoc",
        "artifactId" : "codesnippet-doclet",
        "version" : "1.0",
      },
      "digest": "sha512:6d4d4cf1a59e200a05b11d03fe61656401ddf76cac8a4017d83c478381c5ac727922709c7d2c511281e89a7de636e3bf997bcb22e516232e0ba1f662d0413794",
    },

    "JUNIT" : {
      "digest": "sha512:5974670c3d178a12da5929ba5dd9b4f5ff461bdc1b92618c2c36d53e88650df7adbf3c1684017bb082b477cb8f40f15dcf7526f06f06183f93118ba9ebeaccce",
      "sourceDigest": "sha512:5c36f1671b1567919baa633e01765cf8e67c75f37f52876e11f764e3fccfa7b3c2b4cf2214b8956fd58a06f502694c80a208e8b88bcaca3893fc9c62820322a2",
      "dependencies" : ["HAMCREST"],
      "licence" : "CPL",
      "maven" : {
        "groupId" : "junit",
        "artifactId" : "junit",
        "version" : "4.12",
      }
    },

    "JUNIT-JUPITER": {
      "digest": "sha512:026e582f05e04a6306fa514118bb3e63fadb43927b7873c2375ea34ec6fb8a605c38b16e9e290aabbe59363ce80277d6410cb00f50da1cf38a569e910b66c53a",
      "sourceDigest": "sha512:261e62db845b133ee533676255e3d4961911cd97dba8962e90b580d6fc87b4c813956d50d688341a4e603d3463db0f340e9c440b573222b98a80350821029cd6",
      "license": "EPL-2.0",
      "dependencies": ["JUNIT-JUPITER-API", "JUNIT-JUPITER-PARAMS"],
      "maven": {
        "groupId": "org.junit.jupiter",
        "artifactId": "junit-jupiter",
        "version": "5.8.1",
      }
    },

    "JUNIT-JUPITER-API": {
        "digest": "sha512:4d5248e43e5aba255875c0ca8f529a360f89c9275e58c87de30b5a7c10b569c7eeb1e31401f9be0c2c0b968adb12b2adc6b402aeb99671dc30bbf3a30b0f9924",
        "sourceDigest": "sha512:3c6b0deb3e2d6c11e7c501425dcd5d406ffb03b404cba69c4a8b12879b012f6658f092085db31c69a6f69f02aef370acbdbecf9586064bfb59933914552eefea",
        "license": "EPL-2.0",
        "dependencies": ["APIGUARDIAN-API", "OPENTEST4J"],
        "maven": {
            "groupId": "org.junit.jupiter",
            "artifactId": "junit-jupiter-api",
            "version": "5.8.1",
        }
    },

    "APIGUARDIAN-API": {
        "digest": "sha512:d7ccd0e7019f1a997de39d66dc0ad4efe150428fdd7f4c743c93884f1602a3e90135ad34baea96d5b6d925ad6c0c8487c8e78304f0a089a12383d4a62e2c9a61",
        "sourceDigest": "sha512:0035bb640f97d8c64b9fc085084a94b1c8ffa2dc3145bd59d1ff5cbb2c63ff776569a3fe27bd2e996644223c8748d022e0863ff38391e3b72e82242f123f49a5",
        "license": "EPL-2.0",
        "maven": {
            "groupId": "org.apiguardian",
            "artifactId": "apiguardian-api",
            "version": "1.1.2",
        }
    },

    "OPENTEST4J": {
        "digest": "sha512:17f77797a260eb2bd1666a90e25efc79a5413afa9df1c1cb6c4cd1949d61c38b241e3bb20956396b5f54d144720303d72a2ac00bc5bf245a260a3c3099e01c74",
        "sourceDigest": "sha512:273324c995654f0c7edc5dbf7cd9233f7f3fe400c45e042669f3c25d6476485a738e6baf8f61d08e8a5559dd0b07deae77849059d910d53deabd36424d0fa4ab",
        "license": "EPL-2.0",
        "dependencies": ["JUNIT-PLATFORM-COMMONS"],
        "maven": {
            "groupId": "org.opentest4j",
            "artifactId": "opentest4j",
            "version": "1.2.0",
        }
    },

    "JUNIT-PLATFORM-COMMONS": {
        "digest": "sha512:bb838b278ad803de6443b7331718786b530d241d79170b3898c7d2f199aec81f5a6d4895bf15210f0060b1d5cc7958b184c8c73dd73cfc60fe988557f5d62da5",
        "sourceDigest": "sha512:174ca66db180f8145d134956926bde994a13c81c26d6524c1b9dd8ddd5722b2fbeeec76a53e40193303e9aa030015afcb52529bea5d7c73c1605f222a52b1dd4",
        "license": "EPL-2.0",
        "dependencies": ["APIGUARDIAN-API"],
        "maven": {
            "groupId": "org.junit.platform",
            "artifactId": "junit-platform-commons",
            "version": "1.8.1",
        }
    },

    "JUNIT-JUPITER-PARAMS": {
      "digest": "sha512:7829e36b9bbe910274e46a1424f0e99fb15c584320de1264d26793b1cd857de3d5125da08880fca9a20492adeed6feaa343e40c65607ab4f448395f5835d7b75",
      "sourceDigest": "sha512:06b8679489377d310272c9dc51a5eb676128b52a52ae4ec4c3257e33f6603f5b882d08455d42bbcb4d21a397cb7f9aea08af3ac932bda43d8f9cd2f2659918c4",
      "license": "EPL-2.0",
      "dependencies": ["APIGUARDIAN-API"],
      "maven": {
        "groupId": "org.junit.jupiter",
        "artifactId": "junit-jupiter-params",
        "version": "5.8.1",
      }
    },

    "JUNIT-PLATFORM-ENGINE": {
      "digest": "sha512:840d67896a10a70de95eaf3e0bbd267f30d2ffed19672162bdc8c62deaf8d25731ccb8b33dae46b746e90e7e93c99f95923ba64a18ea61bfdee4abe6353d6a9a",
      "sourceDigest": "sha512:c63dd816d00db7c08c87a6f8757ecd7bc73c519af41b60389720f44fcf34df003a8beb7b7c29742ed0a9fd0fe4629a9f874fc1826f7a816c7212d9dc396a799c",
      "license": "EPL-2.0",
      "dependencies": ["APIGUARDIAN-API", "OPENTEST4J"],
      "maven": {
        "groupId": "org.junit.platform",
        "artifactId": "junit-platform-engine",
        "version": "1.8.1",
      }
    },

    "JUNIT-JUPITER-ENGINE": {
      "digest": "sha512:e98d1b5fa352bef630c07fdb42da582633b9fc092cbe7ab273da3dd7b33c812f61c31882afcdafd8ceb917f272b136065d92a4b2f545d01bfa4396809ee3aecd",
      "sourceDigest": "sha512:5bef574a3a7c03c46c730c62f5b7924f21ae13dbb500517550ec642ef584416c4b01bb8854d49715bd6ffdca5987d0895c2fb25ebfc64a98903c33225109b6bc",
      "license": "EPL-2.0",
      "dependencies": ["JUNIT-JUPITER-API", "APIGUARDIAN-API", "JUNIT-PLATFORM-ENGINE"],
      "maven": {
        "groupId": "org.junit.jupiter",
        "artifactId": "junit-jupiter-engine",
        "version": "5.8.1",
      }
    },

    "JUNIT-VINTAGE-ENGINE": {
      "digest": "sha512:6834862e5caf911526ed6bfc561c80f3b1724d8ba0e81873ba77a2541216a5c120c80fc5632978e5669ceb6558d503cdf4c11c246173d75d09603c524b56745b",
      "sourceDigest": "sha512:42ee3409b1945b81169c07eb49ecdfcb178be11370c5f43135d0c8b311beeb0ccb72d44f542dcc615e6c00a3210041da61a33d6b00cb73f18cd259bc70340cfc",
      "license": "EPL-2.0",
      "dependencies": ["JUNIT", "APIGUARDIAN-API", "JUNIT-PLATFORM-ENGINE"],
      "maven": {
        "groupId": "org.junit.vintage",
        "artifactId": "junit-vintage-engine",
        "version": "5.8.1",
      }
    },

    "JUNIT-PLATFORM-LAUNCHER": {
      "digest": "sha512:e62eb394b84e23287364c101757c44263ce76f99ca08fc7d14c6148b3b46dd0f53291cf6ec6355fbf2053325a0747491224f39cb139dac091fdea87f3e8c6ea7",
      "sourceDigest": "sha512:ba3dfb71cb9720784742ee2431dd1df0dc1b465555aada6aa56a629d75b87b337358ecf3b862909f3c0faba36bfa9b8c98c636161bab274fbd708f8c53b6f9dc",
      "license": "EPL-2.0",
      "dependencies": ["APIGUARDIAN-API", "JUNIT-PLATFORM-ENGINE"],
      "maven": {
        "groupId": "org.junit.platform",
        "artifactId": "junit-platform-launcher",
        "version": "1.8.1",
      }
    },

    "JUNIT-PLATFORM-REPORTING": {
      "digest": "sha512:f772e35a979c4573da43f39178e2f2e537aaa43cf417063fc0da2dcc639ba4566891a2b0725a3ae0e7e8797ea6c661a50121aeb613f19841e212b03833908200",
      "sourceDigest": "sha512:d3662043251d855f39d49dfe3c38157c36d38a6ae0349e7c0d750e73fb96acd8cf6232bc2ed003288556136dd5649d0ab5b10477d21abc56995ffff59a3dd139",
      "license": "EPL-2.0",
      "dependencies": ["APIGUARDIAN-API", "JUNIT-PLATFORM-LAUNCHER"],
      "maven": {
        "groupId": "org.junit.platform",
        "artifactId": "junit-platform-reporting",
        "version": "1.8.1",
      }
    },

    "JUNIT-PLATFORM-CONSOLE": {
      "digest": "sha512:cce0227fdea265f28752934cf89cab7b601bb664cd7101fe9264e9c5cd73afe750ae5eda934c0e5e7c01ebb38ef4a16426be229fbfecaf124447593d766e340e",
      "sourceDigest": "sha512:b815f3a02a803be5d0a98a8fc6d6f8d532262bb0b5696db24b2ff39887298a1a09ea9bb26726366c889ea4cd56d9f91f02d673f85a2ad908e6b953c36d87eed2",
      "license": "EPL-2.0",
      "dependencies": ["APIGUARDIAN-API", "JUNIT-PLATFORM-REPORTING"],
      "maven": {
        "groupId": "org.junit.platform",
        "artifactId": "junit-platform-console",
        "version": "1.8.1",
      }
    },

    "JUNIT-PLATFORM-NATIVE": {
      "digest": "sha512:db9faa6ede8fbf346ad72688b5c446710967c252eda6642d8f900206b9b94c98b69a339b8abaaf7c56da89ae779ebd0e491dc8a999ba7b705e6b16c43c1225f9",
      "sourceDigest": "sha512:a51d02d8460128aa53c40f23620713db376836951a4c22c5eb366d0e223c7311160c7dec0e251e5ba5d2955736e1080e9ff8ab42bf6f6110484ab4675f2d2f9c",
      "license": "UPL",
      "maven": {
        "groupId": "org.graalvm.buildtools",
        "artifactId": "junit-platform-native",
        "version": "0.10.0",
      },
      "dependencies": ["mx:JUNIT-JUPITER", "mx:JUNIT-PLATFORM-CONSOLE", "mx:JUNIT-JUPITER-ENGINE", "mx:JUNIT-VINTAGE-ENGINE"]
    },

    "CHECKSTYLE_6.0" : {
      "urls" : [
        "https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/checkstyle-6.0-all.jar",
        "https://github.com/checkstyle/checkstyle/releases/download/checkstyle-6.0/checkstyle-6.0-all.jar",
      ],
      "digest": "sha512:57ba0a14302e736e8d5d1e4f720ea6b8ee5e49ed811fadb36afe740d441147567ff7e865089b8e47d27af16eafe7def337f9f38e20e8a6ff828a28f713271eb8",
      "licence" : "LGPLv21",
      "maven" : {
        "groupId" : "com.puppycrawl.tools",
        "artifactId" : "checkstyle",
        "version" : "6.0",
      }
    },

    "CHECKSTYLE_6.15" : {
      "urls" : [
        "https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/checkstyle-6.15-all.jar",
        "https://github.com/checkstyle/checkstyle/releases/download/checkstyle-6.15/checkstyle-6.15-all.jar",
      ],
      "digest": "sha512:7cc96c77183d7aa907a8107194843cd64b84643511e50cd1099c954ce1bc182ec16d5b327135e64b28765bd27d1980ee0ceb73d7f3f3d8dea52df0b1281abaf0",
      "licence" : "LGPLv21",
      "maven" : {
        "groupId" : "com.puppycrawl.tools",
        "artifactId" : "checkstyle",
        "version" : "6.15",
      }
    },

    "CHECKSTYLE_8.8" : {
      "urls" : [
        "https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/checkstyle-8.8-all.jar",
        "https://github.com/checkstyle/checkstyle/releases/download/checkstyle-8.8/checkstyle-8.8-all.jar",
      ],
      "digest": "sha512:4484fed4321fc1d96607d453faa3a1435bfffd61b21cc0b3e6e381bca47bcde17b34a55a160820b7deece3bfa67ac92dc53d0fc64576c82ffaeae1e80b033ca6",
      "licence" : "LGPLv21",
      "maven" : {
        "groupId" : "com.puppycrawl.tools",
        "artifactId" : "checkstyle",
        "version" : "8.8",
      }
    },

    "CHECKSTYLE_10.7.0" : {
      "urls" : [
        "https://github.com/checkstyle/checkstyle/releases/download/checkstyle-10.7.0/checkstyle-10.7.0-all.jar"
      ],
      "digest": "sha512:5527f5fca9870d02f691b4d34459386d203558414bdbfb2a117af698101487b4ab6387174e600745a7d1acf0a0358d78bb219d0fba47e4b7ef9365395b0b41b6",
      "licence" : "LGPLv21",
      "maven" : {
        "groupId" : "com.puppycrawl.tools",
        "artifactId" : "checkstyle",
        "version" : "10.7.0",
      }
    },

     "CHECKSTYLE_8.36.1" : {
      "urls" : [
        "https://github.com/checkstyle/checkstyle/releases/download/checkstyle-8.36.1/checkstyle-8.36.1-all.jar"
      ],
      "digest": "sha512:faaacfd79a93586b54064c8b85587d892530fe50a7eb8904cd6e46d8f7d3f253359383f57e9c5788e403a6c9a637f6f52fcf75c006138194efcdbf1962ef5ee7",
      "licence" : "LGPLv21",
      "maven" : {
        "groupId" : "com.puppycrawl.tools",
        "artifactId" : "checkstyle",
        "version" : "8.36.1",
      }
    },

    "HAMCREST" : {
      "digest": "sha512:e237ae735aac4fa5a7253ec693191f42ef7ddce384c11d29fbf605981c0be077d086757409acad53cb5b9e53d86a07cc428d459ff0f5b00d32a8cbbca390be49",
      "sourceDigest": "sha512:38553c75f18f7b39ec86b6c0ce468c775c858f3b7fe234e6bdba1f36a089953a69ea9b645afa34eedb67e0f27e016cde084c2f194d466bc930445de6f7e3fef4",
      "licence" : "BSD-new",
      "maven" : {
        "groupId" : "org.hamcrest",
        "artifactId" : "hamcrest-core",
        "version" : "1.3",
      }
    },

    "COMMONS_MATH3_3_2" : {
      "digest": "sha512:80fb66a51688c4247b957f9787921e5acb9144d71a4ab0b03b2c30f46427e50c53e6e31ca5ddb04dab2cf5e7c0eedae168103c719f8074be464918ab2e4d6e6d",
      "sourceDigest": "sha512:bbb9223025a399ea4dd030da20484030c5ac564ff15b463f67165d2aa17aecdb15fb52fe09ce6aa1f896e749730ebe44cb794c2618200fdc8b5bc7dda6837483",
      "licence" : "Apache-2.0",
      "maven" : {
        "groupId" : "org.apache.commons",
        "artifactId" : "commons-math3",
        "version" : "3.2"
      }
    },

    "JOPTSIMPLE_4_6" : {
      "digest": "sha512:18bf59191d7a456e7675c841df8411ebe425da40532e103db95483be5d2a75510d8a38ad9755cdd4e0be27afe7cfd0b358599388a84fcec1ee27e89caa37f5af",
      "sourceDigest": "sha512:bd10f5ba984b2d75334353f2dd093c28455d49ea05a2c6776fa3834adc386545393f016f13b6608e096b4f8546f4b9d1c3c3948d249a4dbb9b89347b144eea7f",
      "licence": "MIT",
      "maven" : {
        "groupId" : "net.sf.jopt-simple",
        "artifactId" : "jopt-simple",
        "version" : "4.6"
      }
    },

    "JMH_GENERATOR_ANNPROCESS_1_18" : {
      "digest": "sha512:554d58fe550862aa07341668b37aa2bc8780630490c67e73512fc53bf8e4c570f6d8866bf0675a6d1503f680aa649303fb12aae6ede5edc73e65f41e01fb5387",
      "sourceDigest": "sha512:d45f26e49a7d0cb97c38362ee07bd98d542abacccb0d4721da6515a810fe4c01bea62cc900d324ac42162076926b24f56f8247133c402956a7522b2e957c9ff1",
      "licence": "GPLv2-CPE",
      "maven" : {
        "groupId" : "org.openjdk.jmh",
        "artifactId" : "jmh-generator-annprocess",
        "version" : "1.18",
      }
    },

    "JMH_GENERATOR_ANNPROCESS_1_21" : {
      "digest": "sha512:352deb5304ad54d8089485ce066e409c689012a0dee5af4fd8511402cd35624dd4cabd507b876115304c0c9824b837e96028500e279ba164480e1195a757b45c",
      "sourceDigest": "sha512:0c4b7187fd7f524ffe3b63708776136bdd4cddafa172e1f571488c5d0fe4a5526e1edf1e74ef7619950620df8b65003577f1ea97b1c10a935e39361e4e4822f0",
      "licence": "GPLv2-CPE",
      "maven" : {
        "groupId" : "org.openjdk.jmh",
        "artifactId" : "jmh-generator-annprocess",
        "version" : "1.21",
      }
    },

    "JMH_1_18" : {
      "digest": "sha512:2c6fecd9b0f2d114cc826849eae626351ebf94b7bdb46c0e3d73e0c6bbfe996640bed5c3eb20d9235f20cff49dd9b7a341512fa9ab30a8f6ce3c70e5263c90ff",
      "sourceDigest": "sha512:e64394608aa51408d02bce6f4c85ef152aae53046b2301eeadbbf398fb76042db169905046b79ada652f54f5188490d7a898bb4fbc5a73fd18be0cc34b644b21",
      "licence": "GPLv2-CPE",
      "dependencies" : ["JOPTSIMPLE_4_6", "JMH_GENERATOR_ANNPROCESS_1_18", "COMMONS_MATH3_3_2"],
      "maven" : {
        "groupId" : "org.openjdk.jmh",
        "artifactId" : "jmh-core",
        "version" : "1.18",
      }
    },

    "JMH_1_21" : {
      "digest": "sha512:81bca9388bdd0612fa65ca85ccaec5ba01738d7e45e76ea90f64dfb89539ad4dbfca064189dcc05a43f0f3f1bd0b6124676968a953ff7989b06232ff8d00574b",
      "sourceDigest": "sha512:899cedb156944cc1da1b291ca4a592ad57f9069e1c27c23db934eb8c0e9495c4616f51a7ca7d718cecb7edc0e60c07e2740163893e1c942bd5b026c8e5f14798",
      "licence": "GPLv2-CPE",
      "dependencies" : ["JOPTSIMPLE_4_6", "JMH_GENERATOR_ANNPROCESS_1_21", "COMMONS_MATH3_3_2"],
      "maven" : {
        "groupId" : "org.openjdk.jmh",
        "artifactId" : "jmh-core",
        "version" : "1.21",
      }
    },

    "JACKPOT" : {
      "digest": "sha512:117e22f1d509ad5eac019111f78a39da4ed0eb6f5211fbec30030fab9a1d77a9dcaca2cc8eb1c9f8351cc4a218c6aba389af637149c1f561299a4f68effccd10",
      "sourceDigest": "sha512:75fc4e3846a51ca5cfa344518a6b369e0830f1a451b320a82d0466a4f341297503fdd758fa4873fa758b06741d87dd60dd616cd66a04a35d70971622da819e67",
      "licence": "Apache-2.0",
      "maven" : {
        "groupId" : "org.apache.netbeans.modules.jackpot30",
        "artifactId" : "tool",
        "version" : "12.5",
      }
    },

    "PROGUARD_BASE_7_1_0" : {
      "digest": "sha512:4d41a822fe37d5d479e43e2416967f7ecb8530f0e4bb4cf8e6e29f7dbf5b8a979b434a255303df1f0135ba3fa63f1348452f9cc0a1603352aca8bab11facbf46",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-base",
        "version" : "7.1.0",
      }
    },

    "PROGUARD_CORE_7_1_0" : {
      "digest": "sha512:55e47990ce6b141b6892921853e84a109166c1292b0c9003e4afd6d2c8422d944622b337e199da501ef4954dcb3d555ddb0806924f516a7752faaab0a8f26322",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-core",
        "version" : "7.1.0",
      }
    },

    "PROGUARD_RETRACE_7_1_0" : {
      "digest": "sha512:c9b5ee54b8295c0c9b49c866d7cebde14f4bb9d0adcc1715e0e0278c401750393bc5c15921e891c97420c5b8938ff4a9c66080ae393c4a9da6d2864da1970714",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-retrace",
        "version" : "7.1.0",
      }
    },

    "LOG4J_API_2_15_0" : {
      "digest": "sha512:39f88d089c5c7ce85e326aba1b32ace0a21e540fd4580c9c1e1b483251cb945aa568fa8ea3b0f82e3392ce13433c4c5626d0b6be909593774d71cded64483f15",
      "maven" : {
        "groupId" : "org.apache.logging.log4j",
        "artifactId" : "log4j-api",
        "version" : "2.15.0",
      }
    },

    "LOG4J_CORE_2_15_0" : {
      "digest": "sha512:7dd3c6d0e8f0bd4cd7d0e54ac515611ee2796d720a75f8b1b8b582eb1ef6bb5e736685c4e1c18fa70f3f9301acfc5b683aa72062321df6d906cd4be9b046fa85",
      "maven" : {
        "groupId" : "org.apache.logging.log4j",
        "artifactId" : "log4j-core",
        "version" : "2.15.0",
      }
    },

    "LOG4J_API_2_17_1" : {
      "digest": "sha512:48a58c2f317d451ac1622bdfbfa5d3cd9de45d40d5d5df98f39fe6d53c74da56e200f8e3d19a309d4e1ea364369379c0ef9d79b928fc20ea743857f347259c03",
      "maven" : {
        "groupId" : "org.apache.logging.log4j",
        "artifactId" : "log4j-api",
        "version" : "2.17.1",
      }
    },

    "LOG4J_CORE_2_17_1" : {
      "digest": "sha512:8d3d6a17afc41cde43b19c9a696793d009d9271bc6430762f10157018453f8a53cde6e6aa4f3f0b703eaf1f2944d047398d29b470924ecc3290d1923b0e29750",
      "maven" : {
        "groupId" : "org.apache.logging.log4j",
        "artifactId" : "log4j-core",
        "version" : "2.17.1",
      }
    },

    "LOG4J_API_2_19_0" : {
      "digest": "sha512:f7cf3647ed90de7fdef377e4321aa9b9ea2512a46d99109b359f7fc5dcfe6d3ae9f879c212707ea4fd16d358d10d21c56d5178ec4803504745de6fe48c66c3f7",
      "maven" : {
        "groupId" : "org.apache.logging.log4j",
        "artifactId" : "log4j-api",
        "version" : "2.19.0",
      }
    },

    "LOG4J_CORE_2_19_0" : {
      "digest": "sha512:1300ada6f86818ef4dcd17448a8965c1c6dd41ec414de2b2a5bafdf25d03c12100fa9e8f422d7b346f2984e5dfb3d599f8c1a971a6bcaca0cf938943d06364e7",
      "maven" : {
        "groupId" : "org.apache.logging.log4j",
        "artifactId" : "log4j-core",
        "version" : "2.19.0",
      }
    },

    "ORG_JSON_20211205" : {
      "digest": "sha512:bcfada5d9f87bd6494e2c9b4d8da2a700b262eb2541296cf5f38a6e4c8dddf496f1db4bb8b10277dcdf8882a7942ab84b5d73e636312c2b193cf3d5d2969ef82",
      "maven" : {
        "groupId" : "org.json",
        "artifactId" : "json",
        "version" : "20211205",
      }
    },

    # As of 8.0.0, the versioning of ProGuardCORE is unlinked from ProguardBASE and ProguardRETRACE
    # since ProGuardCORE is a general library used by other projects.
    # https://github.com/Guardsquare/proguard/issues/132#issuecomment-887610759
    "PROGUARD_CORE_8_0_0" : {
      "digest": "sha512:5c6bb0de77cd99a1c18c421754965403f21f59cf8d13276b07ef41a748f1f1a8dca99fd4f16c79ba474fda3425194e7d91c1e9c342f59caafeb978b2f65289f4",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-core",
        "version" : "8.0.0",
      },
      "dependencies" : ["LOG4J_CORE_2_15_0", "LOG4J_API_2_15_0"],
    },

    "PROGUARD_CORE_9_0_3" : {
      "digest": "sha512:a376c1ff1873a7225add0cdb3aa68cae7659854fe7a1005031c9129938ba151bafa0c775f67fc93b2e5b3c5a69d2a36f9d0690a005381b8fe3de29a7eebf0abb",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-core",
        "version" : "9.0.3",
      },
      "dependencies" : ["LOG4J_CORE_2_17_1", "LOG4J_API_2_17_1"],
    },

    "PROGUARD_CORE_9_0_8" : {
      "digest": "sha512:d728792f5d3b1a14ff61f4ff455bf09879dba3edd2e9af66fb738a90ae36cb2d004738564db1f1809d53deba01662a50eb5b66bf1c7df38da59a851c85dd31c5",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-core",
        "version" : "9.0.8",
      },
      "dependencies" : ["LOG4J_CORE_2_19_0", "LOG4J_API_2_19_0"],
    },

    "PROGUARD_RETRACE_7_2_0_beta1" : {
      "digest": "sha512:55157386457f22faf4ea3fe7d9e494a43a7fb4b6865e4db74e3e8f8e4f2d4c781cc8f720eaa4de0f2e92c5e30544f8f0dbe9ad4d654da6de4bb5ffb1f2878c22",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-retrace",
        "version" : "7.2.0-beta1",
      },
      "dependencies" : ["PROGUARD_CORE_8_0_0"],
    },

    "PROGUARD_BASE_7_2_0_beta1" : {
      "digest": "sha512:45d6c9524895041872cf67217f409f855df630d67bbf1ad2ca0cdd88223072090f86f2bda07219dd0170e0c12b1f88c7e5d253e8d36eb9679d31925265ee14d7",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-base",
        "version" : "7.2.0-beta1",
      },
      "dependencies" : ["PROGUARD_CORE_8_0_0"],
    },

    "PROGUARD_RETRACE_7_3_0_beta1" : {
      "digest": "sha512:7b156134f6749ddd3b397be89c62a36f81915d2cfd61eb1185872a8eac776f526418f6dd3e05a5da52c1ce96ff590a4279bc4ab92a522398e047cf5d4d82b7cc",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-retrace",
        "version" : "7.3.0-beta1",
      },
      "dependencies" : ["PROGUARD_BASE_7_3_0_beta1"],
    },

    "PROGUARD_BASE_7_3_0_beta1" : {
      "digest": "sha512:aa1d9ccd1d2ea8ca7f7c7ae21fa8a5c8d0f0e927c6303a2b662890f2968c56f1f445bf378cfa67db23892fdac0468f3a183fef77380c676d3f475cd57578889b",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-base",
        "version" : "7.3.0-beta1",
      },
      "dependencies" : [
        "PROGUARD_CORE_9_0_3",
        "LOG4J_CORE_2_17_1",
        "LOG4J_API_2_17_1",
        "ORG_JSON_20211205"
      ],
    },

    "PROGUARD_BASE_7_3_2_alpha" : {
      "digest": "sha512:0dcdb47379b084a1d8358a837661111497db6919ce014e21e7772749967d996075e90717f49330b0b00374d65e122d0da211b48763d987c130567b676590bab1",
      "urls": ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/proguard-7.3.2-alpha.jar"],
    },

    "PROGUARD_RETRACE_7_3_2_alpha" : {
      "digest": "sha512:f51074ef93c54b9dec6c629f4241ab4fb0e8ebc583b9293f1f95c37bc886a94dcdb95cdfa5eb9ac5e01611c289e7d7f56779627041481dd5c491894f2119313f",
      "urls": ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/retrace-7.3.2-alpha.jar"],
    },

    "PROGUARD_BASE_7_3_2" : {
      "digest": "sha512:1d5c988372930ed5d4b441d9ff3102e278173b01f2552779261d6f76da6cbeebf26c7d5cf53d860112cbf645f9c59b35b122782d5d60c4386c873ff1691a624f",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-base",
        "version" : "7.3.2",
      },
      "dependencies" : [
        "PROGUARD_CORE_9_0_8",
        "LOG4J_CORE_2_19_0",
        "LOG4J_API_2_19_0",
        "ORG_JSON_20211205"
      ],
    },

    "PROGUARD_RETRACE_7_3_2" : {
      "digest": "sha512:5ef65868a441345716a1c4ae7fd78dceb97754246787daadd3edaaae57dcd8c3e9f9c22d1d8a97dc28cf6312214acadac94c0188f22fafbb7b293ec766b83de3",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-retrace",
        "version" : "7.3.2",
      },
      "dependencies" : ["PROGUARD_BASE_7_3_2"],
    },

    "PROGUARD_BASE_7_3_2_JDK21_BACKPORT" : {
      # Identical to PROGUARD_RETRACE_7_3_2 besides the dependency on PROGUARD_CORE_9_0_8_JDK21_BACKPORT
      "digest": "sha512:1d5c988372930ed5d4b441d9ff3102e278173b01f2552779261d6f76da6cbeebf26c7d5cf53d860112cbf645f9c59b35b122782d5d60c4386c873ff1691a624f",
      "maven" : {
        "groupId" : "com.guardsquare",
        "artifactId" : "proguard-base",
        "version" : "7.3.2",
      },
      "dependencies" : [
        "PROGUARD_CORE_9_0_8_JDK21_BACKPORT",
        "LOG4J_CORE_2_19_0",
        "LOG4J_API_2_19_0",
        "ORG_JSON_20211205"
      ],
    },

    "PROGUARD_CORE_9_0_8_JDK21_BACKPORT" : {
      # Built from https://github.com/graalvm/proguard-core/tree/da/jdk21
      "digest": "sha512:4605e7374736faebd71a4c49eb05cbd6da7894630fb037936335767d3b094201638b1ca7052db040b3dd804cf4eff5861d79c130ce8cec4ebf96c1ad42790283",
      "urls": ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/proguard-core-9.0.8-jdk21-backport.jar"],
    },

    "NINJA" : {
      "packedResource" : True,
      "version" : "1.10.2",
      "os_arch" : {
        "linux" : {
          "amd64" : {
            # Built from the same source as https://github.com/ninja-build/ninja/releases/download/v{version}/ninja-linux.zip,
            # but on a system with older glibc for maximum compatibility with older Linux distributions.
            "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/ninja-{version}-linux-amd64.zip"],
            "digest": "sha512:203be0ba85c899530cbf8d27f9f2a2e8247ae3cea66ea3f9f2e2f159cc4583bf424c130791f9ac6d70a4abf53e48291a696704b0670272ceb5ab63d00003acaf"
          },
          "aarch64" : {
            "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/ninja-{version}-linux-aarch64.zip"],
            "digest": "sha512:6592d1c6397a3968df5d473c11c29de040df938a06ac5351f09bdea10fe78a4d171e9dd8be68e62cba30d01b72d575f55b29376b46812e7c4c168df34dbbf76f"
          },
          "<others>" : {
            "optional" : True
          }
        },
        "linux-musl" : {
          # Steps to build:
          # (Built in an Alpine docker container, Alpine version 3.13.0)
          # apk add python2 g++ re2c git
          # mkdir build && cd build
          # git clone https://github.com/ninja-build/ninja && cd ninja
          # git checkout <github release commit of the particular Ninja version>
          # ./configure.py --bootstrap
          "amd64" : {
            "urls" : ["https://lafo.ssw.jku.at/pub/graal-external-deps/ninja-{version}-linux-amd64-musl.zip"],
            "digest": "sha512:5f23099cac6d9e852c2368930ecf0eb859afc17aeba48cbcba844ecb7a020e30aae2f637186544d780a1319162a4b4dc8b230996f19ce0b4f1aeb61be6a56653"
          }
        },
        "darwin" : {
          "amd64" : {
            "urls" : ["https://github.com/ninja-build/ninja/releases/download/v{version}/ninja-mac.zip"],
            "digest": "sha512:bcd12f6a3337591306d1b99a7a25a6933779ba68db79f17c1d3087d7b6308d245daac08df99087ff6be8dc7dd0dcdbb3a50839a144745fa719502b3a7a07260b"
          },
          "aarch64" : {
            "urls" : ["https://github.com/ninja-build/ninja/releases/download/v{version}/ninja-mac.zip"],
            "digest": "sha512:bcd12f6a3337591306d1b99a7a25a6933779ba68db79f17c1d3087d7b6308d245daac08df99087ff6be8dc7dd0dcdbb3a50839a144745fa719502b3a7a07260b"
          }
        },
        "windows" : {
          "amd64" : {
            "urls" : ["https://github.com/ninja-build/ninja/releases/download/v{version}/ninja-win.zip"],
            "digest": "sha512:6004140d92e86afbb17b49c49037ccd0786ce238f340f7d0e62b4b0c29ed0d6ad0bab11feda2094ae849c387d70d63504393714ed0a1f4d3a1f155af7a4f1ba3"
          }
        },
        "solaris" : {
          "<others>" : {
            "optional" : True
          }
        }
      }
    },

    "NINJA_SYNTAX" : {
      "packedResource" : True,
      "version" : "1.7.2",
      "urls" : ["https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/ninja_syntax-1.7.2.tar.gz"],
      "digest": "sha512:8c9756de31a88be913f9bb9ff440c58a5c109721348cb59542fb1eee6f95d99f686121b2ab31622b37683632b1a9391285906e31d13f79b82b9e0980681dee4d"
    },

    "SONARSCANNER_CLI_4_2_0_1873": {
      "digest": "sha512:69311bc54a898aac4631a09945dd5621f86c63f6c747b00fe7ffdf479f11ee89a112be3051196ec17c7bf883c045b0b81abfb4d2807a8be106fa6078bcfeb370",
      "maven": {
        "groupId": "org.sonarsource.scanner.cli",
        "artifactId": "sonar-scanner-cli",
        "version": "4.2.0.1873",
      },
      "licence": "LGPLv30",
    },

    "ASYNC_PROFILER_1.8.3": {
      "packedResource": True,
      "urlbase": "https://lafo.ssw.uni-linz.ac.at/pub/graal-external-deps/async-profiler",
      "os_arch": {
        "linux": {
          "amd64": {
            "digest": "sha512:dd991d57234c55c2b8d6c7cb91a001287a5ea15d76ccafc08c7004fc50ea1231c26a9bcfcb41e4d9a9b18b6b041f57c1ae15c0e1e1a7daab1fff7cb18b504725",
            "urls": ["{urlbase}/async-profiler-1.8.3-linux-x64.tar.gz"],
          },
          "aarch64": {
            "digest": "sha512:7445c9d2ecb0fc568ae490976bf58eebbccec04b5466cc80fc52323bcf2513847e9aef1dc89de95a32896f9953a2007493555123c4dfdfcf85cf112810f70ea5",
            "urls": ["{urlbase}/async-profiler-1.8.3-linux-aarch64.tar.gz"],
          },
          "<others>": {
            "optional": True,
          }
        },
        "darwin": {
          "amd64": {
            "digest": "sha512:3e49b1dd6b3240b6f3653914a2288bedbb5ad88e6476b704c3d055bafa4cbe7ec6f556a7dbc086f18b07ef29d89949bc4d9b8485aa62106c92475c62df2e9395",
            "urls": ["{urlbase}/async-profiler-1.8.3-macos-x64.tar.gz"],
          },
          "aarch64": {
            # GR-34811
            "optional": True,
          },
        },
        "<others>": {
          "<others>": {
            "optional": True,
          },
        }
      },
      "license": "Apache-2.0",
    },

    # last compatible version for JDK 8 - do not upgrade or remove
    "ECJ_3.26": {
      "digest": "sha512:ab441acf5551a7dc81c353eaccb3b3df9e89a48987294d19e39acdb83a5b640fcdff7414cee29f5b96eaa8826647f1d5323e185018fe33a64c402d69c73c9158",
      "maven": {
        "groupId": "org.eclipse.jdt",
        "artifactId": "ecj",
        "version": "3.26.0",
      },
      "licence": "EPL-2.0",
    },

    # compatible version for JDK 11 (no longer compatible with < 11)
    "ECJ_3.27": {
      "digest": "sha512:6ceffd50cbcdd539bc8a31d40f674e8e97995697e5c737bf66119c8921e727562586ea6e451a3e0c504337a6725845ee32bd894383afae3a898ff2b57d1962b2",
      "maven": {
        "groupId": "org.eclipse.jdt",
        "artifactId": "ecj",
        "version": "3.27.0",
      },
      "licence": "EPL-2.0",
    },

    # compatible version for JDK >= 17
    "ECJ_3.32": {
      "digest": "sha512:62b19c6701547cb30922fd336a0d40fb0610279a732a93673910954028b79d69e0e3175494d20d3dae9bf4b844677c6bc5d29f337f45b6988bcfaf93b3787602",
      "maven": {
        "groupId": "org.eclipse.jdt",
        "artifactId": "ecj",
        "version": "3.32.0",
      },
      "licence": "EPL-2.0",
    },

    # compatible version for JDK >= 21
    "ECJ_3.36": {
      "digest": "sha512:f889b0f305cdf6b548e13ef73cd8ec488be3bf43a3d48659a1fcfce01068fb47adb398bb6006a067d61cfefbee7ecc279e4fcea385f27be211817709cdebc54e",
      "maven": {
        "groupId": "org.eclipse.jdt",
        "artifactId": "ecj",
        "version": "3.36.0",
      },
      "licence": "EPL-2.0",
    },

  },

  "licenses" : {
    "GPLv2-CPE" : {
      "name" : "GNU General Public License, version 2, with the Classpath Exception",
      "url" : "http://openjdk.java.net/legal/gplv2+ce.html"
    },
    "BSD-new" : {
      "name" : "New BSD License (3-clause BSD license)",
      "url" : "http://opensource.org/licenses/BSD-3-Clause"
    },
    "CPL" : {
      "name" : "Common Public License Version 1.0",
      "url" : "http://opensource.org/licenses/cpl1.0.txt"
    },
    "LGPLv21" : {
      "name" : "GNU Lesser General Public License, version 2.1",
      "url" : "http://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html"
    },
    "LGPLv30": {
      "name": "GNU Lesser General Public License, version 3.0",
      "url": "http://www.gnu.org/licenses/lgpl-3.0.en.html"
    },
    "MIT" : {
      "name" : "MIT License",
      "url" : "http://opensource.org/licenses/MIT"
    },
    "Apache-2.0" : {
      "name" : "Apache License 2.0",
      "url" : "https://opensource.org/licenses/Apache-2.0"
    },
    "EPL-1.0": {
      "name": "Eclipse Public License 1.0",
      "url": "https://opensource.org/licenses/EPL-1.0",
    },
    "EPL-2.0": {
      "name": "Eclipse Public License 2.0",
      "url": "https://opensource.org/licenses/EPL-2.0",
    },
    "UPL": {
      "name": "Universal Permissive License, Version 1.0",
      "url": "http://opensource.org/licenses/UPL",
    },
  },

  "projects" : {

    "com.oracle.mxtool.jmh_1_21" : {
      "subDir" : "java",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "JMH_1_21",
      ],
      "checkstyle" : "com.oracle.mxtool.junit",
      "javaCompliance" : "1.8+",
      "annotationProcessors" : ["JMH_1_21"],
      "spotbugsIgnoresGenerated" : True,
      "graalCompilerSourceEdition": "ignore",
    },

    "com.oracle.mxtool.junit" : {
      "subDir" : "java",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "JUNIT",
      ],
      "javaCompliance" : "1.8+",
      "checkstyleVersion" : "8.36.1",
      "graalCompilerSourceEdition": "ignore",
    },

    "com.oracle.mxtool.junit.jdk9" : {
      "subDir" : "java",
      "sourceDirs" : ["src"],
      "dependencies" : [
        "JUNIT",
      ],
      "requiresConcealed" : {
        "java.base" : [
          "jdk.internal.module",
        ],
      },
      "multiReleaseJarVersion": "9",
      "overlayTarget" : "com.oracle.mxtool.junit",
      "checkPackagePrefix" : False,
      "javaCompliance" : "9+",
      "checkstyle" : "com.oracle.mxtool.junit",
      "graalCompilerSourceEdition": "ignore",
    },

    "com.oracle.mxtool.compilerserver" : {
      "subDir" : "java",
      "sourceDirs" : ["src"],
      "javaCompliance" : "1.8+",
      "checkstyle" : "com.oracle.mxtool.junit",
    },

    "com.oracle.mxtool.checkcopy" : {
      "subDir" : "java",
      "sourceDirs" : ["src"],
      "javaCompliance" : "1.8+",
      "checkstyle" : "com.oracle.mxtool.junit",
      "graalCompilerSourceEdition": "ignore",
    },

    "com.oracle.mxtool.jacoco" : {
      "subDir" : "java",
      "sourceDirs" : ["src"],
      "javaCompliance" : "1.8+",
      "checkstyle" : "com.oracle.mxtool.junit",
      "dependencies" : [
        "JACOCOREPORT_0.8.10",
        "JOPTSIMPLE_4_6",
      ],
      "graalCompilerSourceEdition": "ignore",
    },

    "com.oracle.mxtool.webserver" : {
      "subDir" : "java",
      "sourceDirs" : ["src"],
      "javaCompliance" : "1.8+",
      "checkstyle" : "com.oracle.mxtool.junit",
      "graalCompilerSourceEdition": "ignore",
    },

    # Native library for HotSpot assembly capture
    "com.oracle.jvmtiasmagent": {
      "subDir": "java",
      "native": "shared_lib",
      "use_jdk_headers": True,
      "os_arch": {
        "linux": {
          "amd64": {
            "cflags" : ["-fPIC", "-Wall", "-Werror", "-O", "-g", "-DJVMTI_ASM_ARCH=amd64", "-std=gnu99"],
            "ldflags" : ["-lrt"],
          },
          "aarch64": {
            "cflags" : ["-fPIC", "-Wall", "-Werror", "-O", "-g", "-DJVMTI_ASM_ARCH=aarch64", "-std=gnu99"],
          },
          "riscv64" : {
            "cflags" : ["-fPIC", "-Wall", "-Werror", "-O", "-g", "-DJVMTI_ASM_ARCH=riscv64", "-std=gnu99"],
          }
        },
        "darwin": {
            "<others>": {
                "ignore": "mac is currently not supported",
            },
        },
        "windows": {
            "<others>": {
                "ignore": "windows is not supported",
            },
        },
      },
      "graalCompilerSourceEdition": "ignore",
    },
   },

  "distributions" : {
    "JUNIT_TOOL" : {
      "subDir" : "java",
      "dependencies" : [
        "com.oracle.mxtool.junit",
      ],
      "exclude" : [
        "JUNIT",
        "HAMCREST",
      ],
      "moduleInfo" : {
        "name" : "com.oracle.mxtool.junit",
      },
      "graalCompilerSourceEdition": "ignore",
    },

    "MX_JACOCO_REPORT" : {
      "subDir" : "java",
      "mainClass" : "com.oracle.mxtool.jacoco.JacocoReport",
      "dependencies" : ["com.oracle.mxtool.jacoco"],
      "graalCompilerSourceEdition": "ignore",
    },

    "MX_MICRO_BENCHMARKS" : {
      "subDir" : "java",
      "dependencies" : ["com.oracle.mxtool.jmh_1_21"],
      "graalCompilerSourceEdition": "ignore",
    },

    "GCC_NINJA_TOOLCHAIN": {
      "native": True,
      "platformDependent": False,
      "description": "ninja rules for a GCC toolchain found on the PATH",
      "layout": {
        "toolchain.ninja": "file:ninja-toolchains/gcc.ninja",
      },
      "maven": False,
      "graalCompilerSourceEdition": "ignore",
    },

    "MSVC_NINJA_TOOLCHAIN": {
      "native": True,
      "platformDependent": False,
      "description": "ninja rules for a MSVC toolchain found on the PATH",
      "layout": {
        "toolchain.ninja": "file:ninja-toolchains/msvc.ninja",
      },
      "maven": False,
      "graalCompilerSourceEdition": "ignore",
    },

    "DEFAULT_NINJA_TOOLCHAIN": {
      "native": True,
      "platformDependent": True,
      "description": "Default ninja rules for an OS-dependent toolchain found on the PATH",
      "native_toolchain": {
        "kind": "ninja",
        "target": {
          # all defaults (host compiler, host os/arch/libc, no variant)
        },
      },
      "os_arch": {
        "<others>": {
          "<others>": {
            "layout": {
              "./": "extracted-dependency:GCC_NINJA_TOOLCHAIN",
            },
            "asm_requires_cpp": False,
          },
        },
        "windows": {
          "<others>": {
            "layout": {
              "./": "extracted-dependency:MSVC_NINJA_TOOLCHAIN",
            },
            "asm_requires_cpp": True,
          },
        },
      },
      "maven": False,
      "graalCompilerSourceEdition": "ignore",
    },
  },
}
