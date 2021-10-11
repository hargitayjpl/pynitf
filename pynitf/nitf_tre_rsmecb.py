from .nitf_tre import Tre, tre_tag_to_cls

hlp = '''This is the RSMECB TRE, blah. 

The field names can be pretty cryptic, but are documented in detail in 
the NITF TRE documentation (STDI-0002 V4.0, available at 
http://www.gwg.nga.mil/ntb/baseline/docs/stdi0002).

There is a table in the main body on page vii that gives the a pointer for 
where in the document a particular TRE is defined.

RSMECB is documented at STDI-0002-1-v5.0 Appendix U, Section 13.7, Table 10
'''

_xuol_format = "%21.14E"

desc = [["iid", "Image Identifier", 80, str, {'optional':True}],
        ["edition", "RSM Image Support Data Edition", 40, str],
        ["tid", "Triangulation ID", 40, str, {'optional':True}],
        ["inclic", "Include Indirect Error Covariance Flag", 1, str],
        ["incluc", "Include Unmodeled Error Covariance Flag", 1, str],
        ["nparo", "Number of Original Adjustable Parameters", 2, int,
         {'condition' : "f.inclic == 'Y'"}],
        ["ign", "Number of Independent Subgroups", 2, int,
         {'condition' : "f.inclic == 'Y'"}],
        ["cvdate", "Version Date of the Original Image Error Covariance.", 8,
         str, {'condition' : "f.inclic == 'Y'"}],
        ["npar", "Number of Active RSM Adjustable Parameters", 2, int,
         {'condition' : "f.inclic == 'Y'"}],
        ["aptyp", "Adjustable Parameter Type", 1, str,
         {'condition' : "f.inclic == 'Y'"}],
        ["loctyp", "Local Coordinate System Identifier", 1, str,
         {'condition' : "f.inclic == 'Y'"}],
        ["nsfx", "Normalization Scale Factor for X", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.inclic == 'Y'"}],
        ["nsfy", "Normalization Scale Factor for Y", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.inclic == 'Y'"}],
        ["nsfz", "Normalization Scale Factor for Z", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.inclic == 'Y'"}],
        ["noffx", "Normalization Offset for X", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.inclic == 'Y'"}],
        ["noffy", "Normalization Offset for Y", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.inclic == 'Y'"}],
        ["noffz", "Normalization Offset for Z", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.inclic == 'Y'"}],
        ["xuol", "Local Coordinate Origin (XUOL).", 21, float,
         {'frmt' : _xuol_format,
          'condition' : "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["yuol", "Local Coordinate Origin (YUOL).", 21, float,
         {'frmt' : _xuol_format,
          'condition' : "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["zuol", "Local Coordinate Origin (ZUOL).", 21, float,
         {'frmt' : _xuol_format,
          'condition' : "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["xuxl", "Local Coordinate Unit Vector (XUXL).", 21, float,
         {'frmt' : _xuol_format,
          'condition' : "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["xuyl", "Local Coordinate Unit Vector (XUYL).", 21, float,
         {'frmt' : _xuol_format, 'condition' :
          "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["xuzl", "Local Coordinate Unit Vector (XUZL).", 21, float,
         {'frmt' : _xuol_format,
          'condition' : "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["yuxl", "Local Coordinate Unit Vector (YUXL).", 21, float,
         {'frmt' : _xuol_format,
          'condition' : "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["yuyl", "Local Coordinate Unit Vector (YUYL).", 21, float,
         {'frmt' : _xuol_format, 'condition' :
          "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["yuzl", "Local Coordinate Unit Vector (YUZL).", 21, float,
         {'frmt' : _xuol_format,
          'condition' : "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["zuxl", "Local Coordinate Unit Vector (ZUXL).", 21, float,
         {'frmt' : _xuol_format,
          'condition' : "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["zuyl", "Local Coordinate Unit Vector (ZUYL).", 21, float,
         {'frmt' : _xuol_format, 'condition' :
          "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["zuzl", "Local Coordinate Unit Vector (ZUZL).", 21, float,
         {'frmt' : _xuol_format,
          'condition' : "f.inclic == 'Y' and f.loctyp == 'R'"}],
        ["apbase", "Basis Option.", 1, str, {'condition' : "f.inclic == 'Y'"}],
        ["nisap", "Number of Image-Space Adjustable Parameters.", 2, int,
         {'condition' : "f.inclic == 'Y' and f.aptyp == 'I'"}],
        ["nisapr", "Number of Image-Space Adjustable Parameters for Image Row Coordinate.", 2, int,
         {'condition' : "f.inclic == 'Y' and f.aptyp == 'I'"}],
        [["loop", "f.nisapr"],
         ["xpwrr", "Row Parameter Power of X.", 1, int],
         ["ypwrr", "Row Parameter Power of Y.", 1, int],
         ["zpwrr", "Row Parameter Power of Z.", 1, int],
         ],
        ["nisapc", "Number of Image-Space Adjustable Parameters for Image Column Coordinate", 2, int,
         {'condition' : "f.inclic == 'Y' and f.aptyp == 'I'"}],
        [["loop", "f.nisapc"],
         ["xpwrc", "Column Parameter Power of X.", 1, int],
         ["ypwrc", "Column Parameter Power of Y.", 1, int],
         ["zpwrc", "Column Parameter Power of Z.", 1, int],
         ],
        ["ngsap", "Number of Ground-Space Adjustable Parameters", 2, int,
         {'condition' : "f.inclic == 'Y' and f.aptyp == 'G'"}],
        [["loop", "f.ngsap"],
         ["gsapid", "Ground-space Adjustable Parameter ID", 4, str],
         ],
        ["nbasis", "Number of Basis Adjustable Parameters", 2, int,
         {'condition' : "f.inclic == 'Y' and f.apbase == 'Y'"}],
        [["loop", "f.npar"],
         [["loop", "f.nbasis"],
          ["ael", "Matrix A Element, Row order", 21, float,
           {'frmt' : _xuol_format}],
          ]
         ],
        [["loop", "f.ign"],
         ["numopg", "Number of Original Adjustable Parameters in Subgroup. ",
          2, int],
         [["loop", "(f.numopg[i1]+1)*f.numopg[i1] // 2"],
          ["errcvg", "Original Error Covariance Element", 21, float,
           {'frmt' : _xuol_format}],
          ],
         ["tcdf", "Time Correlation Domain Flag", 1, int],
         ["acsmc", "CSM Correlation Option", 1, str],
         ["ncseg", "Number of Correlation Segments.", 1, int,
          {'condition' : "f.acsmc[i1] == 'N'"}],
         [["loop","f.ncseg[i1]"],
          ["corseg", "Segment Correlation Value", 21, float,
           {'frmt' : _xuol_format}],
          ["tauseg", "Segment Tau Value", 21, float,
           {'frmt' : _xuol_format}],
          ],
         ["ac", "CSM correlation function A parameter", 21, float,
          {'frmt' : _xuol_format,
           'condition' : "f.inclic == 'Y' and f.acsmc[i1] == 'Y'"}],
         ["alpc", "CSM correlation function alpha parameter", 21, float,
          {'frmt' : _xuol_format,
           'condition' : "f.inclic == 'Y' and f.acsmc[i1] == 'Y'"}],
         ["betc", "CSM correlation function beta parameter", 21, float,
          {'frmt' : _xuol_format,
           'condition' : "f.inclic == 'Y' and f.acsmc[i1] == 'Y'"}],
         ["tc", "CSM correlation function T parameter", 21, float,
          {'frmt' : _xuol_format,
           'condition' : "f.inclic == 'Y' and f.acsmc[i1] == 'Y'"}],
         ],
        [["loop", "f.npar"],
         [["loop", "f.nparo"],
          ["map", "Mapping Matrix Element.", 21, float,
           {'frmt' : _xuol_format}],
          ],
         ],
        ["urr", "Unmodeled Row Variance.", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.incluc == 'Y'"}],
        ["urc", "Unmodeled Row-Col Covariance.", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.incluc == 'Y'"}],
        ["ucc", "Unmodeled Col Variance.", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.incluc == 'Y'"}],
        ["uacsmc", "Unmodeled CSM Correlation Option", 1, str,
         {'condition' : "f.incluc == 'Y'"}],
        ["uncsr", "Number of Correlation Segments for independent variable ROW distance", 1, int,
         {'condition' : "f.incluc == 'Y' and f.uacsmc == 'N'"}],
        [["loop", "f.uncsr"],
         ["ucorsr", "Segment Correlation Value", 21, float,
          {'frmt' : _xuol_format}],
         ["utausr", "Segment Tau Value", 21, float, {'frmt' : _xuol_format}],
         ],
        ["uncsc", "Number of Correlation Segments for independent variable Column distance.", 1, int,
         {'condition' : "f.incluc == 'Y' and f.uacsmc == 'N'"}],
        [["loop", "f.uncsc"],
         ["ucorsc", "Segment Correlation Value", 21, float,
          {'frmt' : _xuol_format}],
         ["utausc", "Segment Tau Value.", 21, float, {'frmt' : _xuol_format}],
         ],
        ["uacr", "CSM correlation function A parameter", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.incluc == 'Y' and f.uacsmc == 'Y'"}],
        ["ualpcr", "CSM correlation function alpha parameter", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.incluc == 'Y' and f.uacsmc == 'Y'"}],
        ["ubetcr", "CSM correlation function beta parameter", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.incluc == 'Y' and f.uacsmc == 'Y'"}],
        ["utcr", "CSM correlation function t parameter", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.incluc == 'Y' and f.uacsmc == 'Y'"}],
        ["uacc", "CSM correlation function A parameter", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.incluc == 'Y' and f.uacsmc == 'Y'"}],
        ["ualpcc", "CSM correlation function alpha parameter", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.incluc == 'Y' and f.uacsmc == 'Y'"}],
        ["ubetcc", "CSM correlation function beta parameter", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.incluc == 'Y' and f.uacsmc == 'Y'"}],
        ["utcc", "CSM correlation function t parameter", 21, float,
         {'frmt' : _xuol_format, 'condition' : "f.incluc == 'Y' and f.uacsmc == 'Y'"}],
]

class TreRSMECB(Tre):
    __doc__ = hlp
    desc = desc
    tre_tag = "RSMECB"

tre_tag_to_cls.add_cls(TreRSMECB)    

__all__ = [ "TreRSMECB", ]