// File Information Interfaces
interface FileFormat {
    Vector: string[];
    Raster: string[];
}

interface CameraSettings {
    Aperture: string;
    ShutterSpeed: string;
    ISO: string;
    WhiteBalance: string;
    FocalLength: string;
}

interface Camera {
    Make: string;
    Model: string;
    Settings: CameraSettings;
}

interface GPS {
    Latitude: number;
    Longitude: number;
    Altitude: number;
}

interface Lens {
    Make: string;
    Model: string;
    FocalLength: string;
    ApertureRange: string;
}

interface Flash {
    FlashUsed: boolean;
    FlashMode: string;
}

interface Metadata {
    Title: string;
    Author: string;
    Description: string;
    Keywords: string[];
    DateTime: string;
    Camera: Camera;
    GPS: GPS;
    Orientation: string;
    Software: string;
    Copyright: string;
    Lens: Lens;
    Flash: Flash;
    Thumbnail: string;
    ICCProfile: any;  // Specific structure depends on ICC Profile data
    Misc: any;  // Any other miscellaneous metadata information
}

interface Checksum {
    MD5: string;
    SHA1: string;
    SHA256: string;
}

interface Permissions {
    Read: boolean;
    Write: boolean;
    Execute: boolean;
}

interface FileInformation {
    FileName: string;
    FileSize: string;
    CreationDate: string;
    LastModifiedDate: string;
    FileFormat: FileFormat;
    Metadata: Metadata;
    Checksum: Checksum;
    Permissions: Permissions;
    VersionNumber: string;
    ChangeLog: string[];
    LinkedFiles: string[];
    EmbeddedFonts: string[];
    AdobeXMP: string;
    HistoryLog: string;
}

// Image Specifications Interfaces
interface Dimensions {
    Width: number;
    Height: number;
}

interface Margins {
    Top: number;
    Bottom: number;
    Left: number;
    Right: number;
}

interface Histogram {
    Red: any;  // Specific structure depends on Histogram data
    Green: any;  // Specific structure depends on Histogram data
    Blue: any;  // Specific structure depends on Histogram data
}

interface ImageSpecifications {
    Resolution: number;
    AspectRatio: string;
    ColorSpace: string;
    NumberOfColors: number;
    Dimensions: Dimensions;
    Orientation: string;
    Margins: Margins;
    Artboards: any[];  // Specific structure depends on Artboard data
    PathsShapesTextItems: any[];  // Specific structure depends on Paths, Shapes, and Text Items data
    ObjectCount: number;
    CompressionType: string;
    CompressionRatio: string;
    ColorDepth: number;
    Histogram: Histogram;
    Palette: any[];  // Specific structure depends on Palette data
}

// Color Management Interfaces
interface ColorManagement {
    ICCProfile: string;
    ColorMatchingMethod: string;
    Swatches: any[];  // Specific structure depends on Swatches data
    SpotColors: string;
}

// Cutting Specifications Interfaces
interface RegistrationMarks {
    Type: string;
    Dimensions: Dimensions;
}

interface CuttingSpecifications {
    CuttingPaths: boolean;
    Layers: boolean;
    RegistrationMarks: RegistrationMarks;
}

// Media Specifications Interfaces
interface MediaSpecifications {
    MediaType: string;
    MediaThickness: number;
}

// Content Analysis Interfaces
interface ContentAnalysis {
    LayerAnalysis: any[];  // Specific structure depends on Layer Analysis data
    ColorPalette: any[];  // Specific structure depends on Color Palette data
    Transparency: string;
    BoundingBoxes: any[];  // Specific structure depends on Bounding Boxes data
    LinkedItems: any[];  // Specific structure depends on Linked Items data
    PlacedItems: any[];  // Specific structure depends on Placed Items data
    LayerComps: any[];  // Specific structure depends on Layer Comps data
    LayerEffects: any[];  // Specific structure depends on Layer Effects data
    Guides: any[];  // Specific structure depends on Guides data
    GridSettings: string;
}

// Text Information Interfaces
interface TextInformation {
    FontUsage: any[];  // Specific structure depends on Font Usage data
    TextContent: string;
}

// Document Setup Interfaces
interface DocumentSetup {
    Bleed: number;
    Slug: number;
}

// Output Intent Interfaces
interface OutputIntent {
    OutputProfiles: any[];  // Specific structure depends on Output Profiles data
}

// Resource Utilization Interfaces
interface ResourceUtilization {
    LinkedResourceSize: number;
}

// Software Compatibility Interfaces
interface SoftwareCompatibility {
    Software: string;
    Version: string;
    AdobeFileFormat: string[];
}

// Workflow Automation Interfaces
interface WorkflowAutomation {
    Automated: boolean;
}

// Main Interface
interface ImageFile {
    FileInformation: FileInformation;
    ImageSpecifications: ImageSpecifications;
    ColorManagement: ColorManagement;
    CuttingSpecifications: CuttingSpecifications;
    MediaSpecifications: MediaSpecifications;
    ContentAnalysis: ContentAnalysis;
    TextInformation: TextInformation;
    DocumentSetup: DocumentSetup;
    OutputIntent: OutputIntent;
    ResourceUtilization: ResourceUtilization;
    SoftwareCompatibility: SoftwareCompatibility;
    WorkflowAutomation: WorkflowAutomation;
}

// Constant Object
const imageFile: ImageFile = {
    FileInformation: {
        FileName: "image.png",
        FileSize: "2048000",
        CreationDate: "2023-10-21T14:30:00",
        LastModifiedDate: "2023-10-21T14:45:00",
        FileFormat: {
            Vector: ["EPS", "PDF"],
            Raster: ["TIFF", "JPEG"]
        },
        Metadata: {
            Title: "City Sunset",
            Author: "Photographer Name",
            Description: "A beautiful sunset over the city.",
            Keywords: ["sunset", "city", "scenery"],
            DateTime: "2023-10-21T14:30:00",
            Camera: {
                Make: "Canon",
                Model: "EOS 5D Mark IV",
                Settings: {
                    Aperture: "f/8.0",
                    ShutterSpeed: "1/200",
                    ISO: "400",
                    WhiteBalance: "Auto",
                    FocalLength: "50mm"
                }
            },
            GPS: {
                Latitude: 40.748817,
                Longitude: -73.985428,
                Altitude: 10
            },
            Orientation: "Normal",
            Software: "Adobe Photoshop CC 2023",
            Copyright: "Copyright 2023, Photographer Name",
            Lens: {
                Make: "Canon",
                Model: "EF 50mm f/1.4 USM",
                FocalLength: "50mm",
                ApertureRange: "f/1.4 - f/22"
            },
            Flash: {
                FlashUsed: false,
                FlashMode: "Off"
            },
            Thumbnail: "Base64 or URL",
            ICCProfile: { /* ICC Profile Data */ },
            Misc: { /* Any other miscellaneous metadata information */ }
        },
        Checksum: "e99a18c428cb38d5f260853678922e03",
        Permissions: "Read/Write",
        VersionNumber: "1.0",
        ChangeLog: "Initial version",
        LinkedFiles: [],
        EmbeddedFonts: [],
        AdobeXMP: "XMP data here",
        HistoryLog: "History log here"
    },
    ImageSpecifications: {
        Resolution: 300,
        AspectRatio: "1:1",
        ColorSpace: "sRGB",
        NumberOfColors: "16777216",
        Dimensions: {
            Width: "1920",
            Height: "1080"
        },
        Orientation: "Portrait",
        Margins: {
            Top: "0.5",
            Bottom: "0.5",
            Left: "0.5",
            Right: "0.5"
        },
        Artboards: [],  // Assuming no artboards data
        PathsShapesTextItems: [],  // Assuming no paths, shapes, and text items data
        ObjectCount: "3",
        CompressionType: "Lossless",
        CompressionRatio: "1:1",
        ColorDepth: "24",
        Histogram: {
            Red: { /* Histogram Data */ },
            Green: { /* Histogram Data */ },
            Blue: { /* Histogram Data */ }
        },
        Palette: []  // Assuming no palette data
    },
    ColorManagement: {
        ICCProfile: "Adobe RGB (1998)",
        ColorMatchingMethod: "Relative Colorimetric",
        Swatches: [],  // Assuming no swatches data
        SpotColors: "None"
    },
    CuttingSpecifications: {
        CuttingPaths: true,
        Layers: true,
        RegistrationMarks: {
            Type: "Crosshair",
            Dimensions: {
                Width: "0.5",
                Height: "0.5"
            }
        }
    },
    MediaSpecifications: {
        MediaType: "Vinyl",
        MediaThickness: "0.08"
    },
    ContentAnalysis: {
        LayerAnalysis: [],  // Assuming no layer analysis data
        ColorPalette: [],  // Assuming no color palette data
        Transparency: "None",
        BoundingBoxes: [],  // Assuming no bounding boxes data
        LinkedItems: [],  // Assuming no linked items data
        PlacedItems: [],  // Assuming no placed items data
        LayerComps: [],  // Assuming no layer comps data
        LayerEffects: [],  // Assuming no layer effects data
        Guides: [],  // Assuming no guides data
        GridSettings: "Default"
    },
    TextInformation: {
        FontUsage: [],  // Assuming no font usage data
        TextContent: "None"
    },
    DocumentSetup: {
        Bleed: "0.125",
        Slug: "0.25"
    },
    OutputIntent: {
        OutputProfiles: []  // Assuming no output profiles data
    },
    ResourceUtilization: {
        LinkedResourceSize: "0"
    },
    SoftwareCompatibility: {
        Software: "Adobe Illustrator",
        Version: "CC 2022",
        AdobeFileFormat: ["AI", "PDF", "EPS"]
    },
    WorkflowAutomation: {
        Automated: true
    }
};
