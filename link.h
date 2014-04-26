/*  This file is part of Misli.

    Misli is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Misli is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Misli.  If not, see <http://www.gnu.org/licenses/>.
*/

#ifndef LINK_H
#define LINK_H

#include <QString>

class Link
{
public:
    //Functions
    Link();
    ~Link();

    //Hard variables
    int id;
    QString text;

    //Program variables
    float x1,y1,z1,x2,y2,z2;
    bool selected;
};

#endif // LINK_H
