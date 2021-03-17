"""
    Inherited exchange object.
    Copyright (C) 2021  Emerson Dove

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import json


class Exchange:
    def __init__(self, exchange_type, exchange_name):
        self.__name = exchange_name
        self.__type = exchange_type
        try:
            f = open("Settings.json",)
            self.__preferences = json.load(f)
        except FileNotFoundError as e:
            FileNotFoundError("Place a Settings.json file in the same directory as the Blankly bot main class")


    def get_name(self):
        return self.__name

    def getType(self):
        return self.__type

    def getPreferences(self):
        return self.__preferences