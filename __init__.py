# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GPIImport
                                 A QGIS plugin
 GPIImport
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-11-11
        copyright            : (C) 2019 by gerd 3er geoplaning GmbH
        email                : kontakt@geoplaning.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GPIImport class from file GPIImport.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gpi_import import GPIImport
    return GPIImport(iface)
