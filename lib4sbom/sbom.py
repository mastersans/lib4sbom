# Copyright (C) 2023 Anthony Harrison
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List, NamedTuple


class SBOMData(NamedTuple):
    document: List
    files: Dict
    packages: Dict
    relationships: List
    type: str
    version: str


class SBOM:
    """
    Simple SBOM Object.
    """

    def __init__(self, sbom_type: str = "auto"):
        self.sbom = {}
        self.set_type(sbom_type)

    def add_document(self, document: Dict):
        self.sbom["document"] = document

    def add_files(self, files: Dict):
        self.sbom["files"] = files

    def add_packages(self, packages: Dict):
        self.sbom["packages"] = packages
        # print (f"Added package {self.sbom}")

    def add_relationships(self, relationships: List):
        self.sbom["relationships"] = relationships

    def add_data(self, sbom_data: SBOMData) -> None:
        for key, value in sbom_data.items():
            self.sbom[key] = value
        print(f"AD {self.sbom}")

    def set_type(self, sbom_type):
        self.sbom["type"] = sbom_type

    def set_version(self, version):
        self.sbom["version"] = version

    def get_sbom(self) -> SBOMData:
        return self.sbom

    def get_document(self) -> List:
        return self.sbom["document"]

    def get_files(self) -> Dict:
        # return self.sbom['files'
        return [x for x in self.sbom["files"].values()]

    def get_packages(self) -> Dict:
        # return self.sbom['packages']
        return [x for x in self.sbom["packages"].values()]

    def get_relationships(self) -> List:
        # return self.sbom['relationships']
        return self.sbom["relationships"]

    def get_version(self) -> str:
        return self.sbom["version"]

    def get_type(self) -> str:
        return self.sbom["type"]