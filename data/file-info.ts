interface FileInformation {
    FileName: string;
    FileSize: string;
    FileFormat: string;
    FileExtension: string;
    CreationDate: string;
    LastModifiedDate: string;
    Checksum: {
        MD5: string;
        SHA1: string;
        SHA256: string;
    };
    Permissions: {
        Read: string;
        Write: string;
        Execute: string;
    };
    VersionNumber: string;
    ChangeLog: string[];
    Metadata: {
        Title: string;
        Author: string;
        Description: string;
        Keywords: string[];
        Language: string;
    };
    FileDependencies: {
        LinkedFiles: string[];
        EmbeddedFiles: string[];
        EmbeddedFonts: string[];
    };
    FileHistory: {
        PreviousVersions: string[];
        RevisionComments: string[];
    };
    FileSignature: string;
    FileComments: string[];
    CustomMetadata: Record<string, unknown>;
    Hierarchy: {
        ParentFile: string;
        ChildFiles: string[];
        Project: {
            ProjectName: string;
            ProjectID: string;
            ProjectMetadata: Record<string, unknown>;
        };
    };
    CrossReferences: {
        ReferencedBy: string[];
        References: string[];
    };
    Security: {
        Encryption: {
            Algorithm: string;
            Key: string;
            Certificate: string;
        };
        AccessControls: {
            ACL: string[];
        };
    };
    UsageStats: {
        AccessCount: number;
        LastAccessed: string;
        ModifiedBy: string[];
    };
    Location: {
        PhysicalLocation: string;
        LogicalLocation: string;
    };
}

interface SoftwareInformation {
    SoftwareName: string;
    SoftwareVersion: string;
    SoftwareVendor: string;
    Extensions: {
        Plugins: string[];
        Addons: string[];
    };
}

interface OperatingSystem {
    OSName: string;
    OSVersion: string;
    NetworkConfiguration: {
        IP: string;
        Subnet: string;
        Gateway: string;
    };
}

interface Compatibility {
    SupportedSoftwareVersions: string[];
    SupportedOSVersions: string[];
}

interface FileInfo {
    FileInformation: FileInformation;
    SoftwareInformation: SoftwareInformation;
    OperatingSystem: OperatingSystem;
    Compatibility: Compatibility;
}

const fileInfo: FileInfo = {
    FileInformation: {
        FileName: "",
        FileSize: "",
        FileFormat: "",
        FileExtension: "",
        CreationDate: "",
        LastModifiedDate: "",
        Checksum: {
            MD5: "",
            SHA1: "",
            SHA256: ""
        },
        Permissions: {
            Read: "",
            Write: "",
            Execute: ""
        },
        VersionNumber: "",
        ChangeLog: [],
        Metadata: {
            Title: "",
            Author: "",
            Description: "",
            Keywords: [],
            Language: ""
        },
        FileDependencies: {
            LinkedFiles: [],
            EmbeddedFiles: [],
            EmbeddedFonts: []
        },
        FileHistory: {
            PreviousVersions: [],
            RevisionComments: []
        },
        FileSignature: "",
        FileComments: [],
        CustomMetadata: {},
        Hierarchy: {
            ParentFile: "",
            ChildFiles: [],
            Project: {
                ProjectName: "",
                ProjectID: "",
                ProjectMetadata: {}
            }
        },
        CrossReferences: {
            ReferencedBy: [],
            References: []
        },
        Security: {
            Encryption: {
                Algorithm: "",
                Key: "",
                Certificate: ""
            },
            AccessControls: {
                ACL: []
            }
        },
        UsageStats: {
            AccessCount: 0,
            LastAccessed: "",
            ModifiedBy: []
        },
        Location: {
            PhysicalLocation: "",
            LogicalLocation: ""
        }
    },
    SoftwareInformation: {
        SoftwareName: "",
        SoftwareVersion: "",
        SoftwareVendor: "",
        Extensions: {
            Plugins: [],
            Addons: []
        }
    },
    OperatingSystem: {
        OSName: "",
        OSVersion: "",
        NetworkConfiguration: {
            IP: "",
            Subnet: "",
            Gateway: ""
        }
    },
    Compatibility: {
        SupportedSoftwareVersions: [],
        SupportedOSVersions: []
    }
};
