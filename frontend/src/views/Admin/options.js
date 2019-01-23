import type { CheckboxOption, RadioOption } from "types";

// -------------------------------------------
// Semester Target
// -------------------------------------------

export type SemesterTarget = RadioOption & {
  apiId: string
};

export const semesterTargetOptions: Array<SemesterTarget> = [
  {
    apiId: "current",
    label: "Current semester"
  },
  {
    apiId: "next",
    label: "Next semester"
  },
  {
    apiId: "playground",
    label: "Playground (https://tinyurl.com/yabv58ek)"
  }
];

// -------------------------------------------
// Folder Target
// -------------------------------------------

export type FolderTarget = CheckboxOption & {
  apiId: string,
  sourcePath: ?string,
  targetPath: ?string
};

export const folderTargetOptions: Array<FolderTarget> = [
  {
    apiId: "committeeChairs",
    label: "Committee chair folders",
    checked: true,
    sourcePath: null,
    targetPath: null
  },
  {
    apiId: "committeeLeads",
    label: "Committee lead folders",
    checked: true,
    sourcePath: null,
    targetPath: null
  },
  {
    apiId: "missionTeams",
    label: "Mission team folders",
    checked: true,
    sourcePath: null,
    targetPath: null
  },
  {
    apiId: "sectionLeads",
    label: "Section lead folders",
    checked: true,
    sourcePath: null,
    targetPath: null
  }
];

// -------------------------------------------
// Semester Target
// -------------------------------------------

export type MimeType = RadioOption & {
  apiId: string,
  needsExtension: boolean
};

export const mimeTypeOptions: Array<MimeType> = [
  {
    apiId: "gdoc",
    label: "Google Doc",
    needsExtension: false
  },
  {
    apiId: "gsheet",
    label: "Google Sheet",
    needsExtension: false
  },
  {
    apiId: "gslide",
    label: "Google Slides",
    needsExtension: false
  },
  {
    apiId: "gform",
    label: "Google Form",
    needsExtension: false
  },
  {
    apiId: "file",
    label: "Other",
    needsExtension: true
  }
];

// -------------------------------------------
// Action
// -------------------------------------------

export type Action = RadioOption & {
  isFile: boolean,
  needsGlobalSource: boolean, // i.e. source can come from anywhere
  needsFolderSource: boolean, // i.e. source comes from within FolderTarget
  api: string
};

export const actionOptions: Array<Action> = [
  {
    label: "Create empty file",
    isFile: true,
    needsGlobalSource: false,
    needsFolderSource: false,
    api: "/create/file"
  },
  {
    label: "Create empty folder",
    isFile: false,
    needsGlobalSource: false,
    needsFolderSource: false,
    api: "/create/folder"
  },
  {
    label: "Copy file",
    isFile: true,
    needsGlobalSource: true,
    needsFolderSource: false,
    api: "/copy/file"
  },
  {
    label: "Move file",
    isFile: true,
    needsGlobalSource: false,
    needsFolderSource: true,
    api: "/move/file"
  },
  {
    label: "Move folder",
    isFile: false,
    needsGlobalSource: false,
    needsFolderSource: true,
    api: "/move/folder"
  },
  {
    label: "Remove file",
    isFile: true,
    needsGlobalSource: false,
    needsFolderSource: false,
    api: "/remove/file"
  },
  {
    label: "Remove folder",
    isFile: false,
    needsGlobalSource: false,
    needsFolderSource: false,
    api: "/remove/folder"
  },
  {
    label: "Rename file",
    isFile: true,
    needsGlobalSource: false,
    needsFolderSource: true,
    api: "/rename/file"
  },
  {
    label: "Rename folder",
    isFile: false,
    needsGlobalSource: false,
    needsFolderSource: true,
    api: "/rename/folder"
  }
];
