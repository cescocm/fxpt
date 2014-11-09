import os
import pymel.core as pm

from fxpt.fx_prefsaver import PrefSaver


WIN_NAME = 'fxpt_pstest_pymel_win'
MAIN_BUTTONS_HEIGHT = 30

CFG_FILENAME = os.path.dirname(__file__) + '/prefsPM.cfg'


# noinspection PyAttributeOutsideInit
class WinPyMelUI(object):

    def __init__(self, ser):
        self.uiCreate()

        self.prefSaver = PrefSaver.PrefSaver(self.createSerializer(ser))
        self.initPrefs()

    def uiCreate(self):

        self.onCloseClicked()

        self.window = pm.window(
            WIN_NAME,
            title='PyMel Window',
            maximizeButton=False
        )

        with self.window:
            with pm.formLayout() as uiLAY_mainForm:
                with pm.scrollLayout(childResizable=True) as self.uiLAY_mainScroll:
                    with pm.columnLayout(adjustableColumn=True):

                        with self.uiCreateFrame('uiLAY_frameCheckBoxes', 'Check Boxes (PMCheckBox)') as self.uiLAY_frameCheckBoxes:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                with pm.rowLayout(numberOfColumns=3):
                                    pm.separator(width=140, style='none')
                                    self.uiCHK_test1 = pm.checkBox('uiCHK_test1', label='test1')
                                    self.uiCHK_test2 = pm.checkBox('uiCHK_test2', label='test2')

                        with self.uiCreateFrame('uiLAY_frameCheckBoxGroups', 'Check Box Groups (PMCheckBoxGrp#)') as self.uiLAY_frameCheckBoxGroups:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                self.uiCHKGRP_test1 = pm.checkBoxGrp(
                                    'uiCHKGRP_test1',
                                    numberOfCheckBoxes=1,
                                    label='PMCheckBoxGrp1',
                                    label1='test1'
                                )
                                self.uiCHKGRP_test2 = pm.checkBoxGrp(
                                    'uiCHKGRP_test2',
                                    numberOfCheckBoxes=2,
                                    label='PMCheckBoxGrp2',
                                    labelArray2=('test1', 'test2')
                                )
                                self.uiCHKGRP_test3 = pm.checkBoxGrp(
                                    'uiCHKGRP_test3',
                                    numberOfCheckBoxes=3,
                                    label='PMCheckBoxGrp3',
                                    labelArray3=('test1', 'test2', 'test3')
                                )
                                self.uiCHKGRP_test4 = pm.checkBoxGrp(
                                    'uiCHKGRP_test4',
                                    numberOfCheckBoxes=4,
                                    label='PMCheckBoxGrp4',
                                    labelArray4=('test1', 'test2', 'test3', 'test4')
                                )

                        with self.uiCreateFrame('uiLAY_frameColorSliders', 'Color Slider Groups (PMColorSliderGrp)') as self.uiLAY_frameColorSliders:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                self.uiCLRGRP_test1 = pm.colorSliderGrp(
                                    'uiCLRGRP_test1',
                                    label='test1'
                                )
                                self.uiCLRGRP_test2 = pm.colorSliderGrp(
                                    'uiCLRGRP_test2',
                                    label='test2'
                                )

                        with self.uiCreateFrame('uiLAY_frameFloatFields', 'Float Fields (PMFloatField)') as self.uiLAY_frameFloatFields:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                with pm.rowLayout(numberOfColumns=3):
                                    pm.separator(width=140, style='none')
                                    self.uiFLF_test1 = pm.floatField('uiFLF_test1')
                                    self.uiFLF_test2 = pm.floatField('uiFLF_test2')

                        with self.uiCreateFrame('uiLAY_frameFloatFieldGroups', 'Float Field Groups (PMFloatFieldGrp#)') as self.uiLAY_frameFloatFieldGroups:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                self.uiFLFGRP_test1 = pm.floatFieldGrp(
                                    'uiFLFGRP_test1',
                                    numberOfFields=1,
                                    label='PMFloatFieldGrp1'
                                )
                                self.uiFLFGRP_test2 = pm.floatFieldGrp(
                                    'uiFLFGRP_test2',
                                    numberOfFields=2,
                                    label='PMFloatFieldGrp2'
                                )
                                self.uiFLFGRP_test3 = pm.floatFieldGrp(
                                    'uiFLFGRP_test3',
                                    numberOfFields=3,
                                    label='PMFloatFieldGrp3'
                                )
                                self.uiFLFGRP_test4 = pm.floatFieldGrp(
                                    'uiFLFGRP_test4',
                                    numberOfFields=4,
                                    label='PMFloatFieldGrp4'
                                )

                        with self.uiCreateFrame('uiLAY_frameFloatScrollBars', 'Float Scroll Bars (PMFloatScrollBar)') as self.uiLAY_frameFloatScrollBars:
                            with pm.columnLayout(adjustableColumn=True):
                                pm.separator(style='none', height=2)
                                self.uiFLSCRL_test1 = pm.floatScrollBar('uiFLSCRL_test1')
                                self.uiFLSCRL_test2 = pm.floatScrollBar('uiFLSCRL_test2')

                        with self.uiCreateFrame('uiLAY_frameFloatSliders', 'Float Sliders (PMFloatSlider)') as self.uiLAY_frameFloatSliders:
                            with pm.columnLayout(adjustableColumn=True):
                                pm.separator(style='none', height=2)
                                self.uiFLTSLD_test1 = pm.floatSlider('uiFLTSLD_test1')
                                self.uiFLTSLD_test2 = pm.floatSlider('uiFLTSLD_test2')

                        with self.uiCreateFrame('uiLAY_frameFloatSliders2', 'Float Sliders2 (PMFloatSlider2)') as self.uiLAY_frameFloatSliders2:
                            with pm.columnLayout():
                                with pm.rowLayout(numberOfColumns=4):
                                    pm.separator(style='none', width=140)
                                    self.uiFLSLD2_test1 = pm.floatSlider2('uiFLSLD2_test1')
                                    pm.separator(style='none', width=50)
                                    self.uiFLSLD2_test2 = pm.floatSlider2('uiFLSLD2_test2')

                        with self.uiCreateFrame('uiLAY_frameFloatSliderGroups', 'Float Slider Groups (PMFloatSliderGrp)') as self.uiLAY_frameFloatSliderGroups:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                self.uiFLSGRP_test1 = pm.floatSliderGrp(
                                    'uiFLSGRP_test1',
                                    label='test1',
                                    field=True
                                )
                                self.uiFLSGRP_test2 = pm.floatSliderGrp(
                                    'uiFLSGRP_test2',
                                    label='test2',
                                    field=True
                                )

                        with self.uiCreateFrame('uiLAY_frameIconTextCheckBoxes', 'Icon Text Check Boxes (PMIconTextCheckBox)') as self.uiLAY_frameIconTextCheckBoxes:
                            with pm.columnLayout():
                                with pm.rowLayout(numberOfColumns=3):
                                    pm.separator(style='none', width=140)
                                    self.uiITCHK_test1 = pm.iconTextCheckBox(
                                        'uiITCHK_test1',
                                        style='iconAndTextHorizontal',
                                        label='cube',
                                        image1='cube'
                                    )
                                    self.uiITCHK_test2 = pm.iconTextCheckBox(
                                        'uiITCHK_test2',
                                        style='iconAndTextHorizontal',
                                        label='cone',
                                        image1='cone'
                                    )

                        with self.uiCreateFrame('uiLAY_frameIconTextRadioButtons', 'Icon Text Radio Buttons (PMIconTextRadioButton)') as self.uiLAY_frameIconTextRadioButtons:
                            with pm.columnLayout():
                                with pm.rowLayout(numberOfColumns=4):
                                    pm.separator(style='none', width=140)
                                    pm.iconTextRadioCollection()
                                    self.uiITRAD_test1 = pm.iconTextRadioButton(
                                        'uiITRAD_test1',
                                        style='iconAndTextHorizontal',
                                        label='cube',
                                        image1='cube'
                                    )
                                    self.uiITRAD_test2 = pm.iconTextRadioButton(
                                        'uiITRAD_test2',
                                        style='iconAndTextHorizontal',
                                        label='cone',
                                        image1='cone'
                                    )
                                    self.uiITRAD_test3 = pm.iconTextRadioButton(
                                        'uiITRAD_test3',
                                        style='iconAndTextHorizontal',
                                        label='torus',
                                        image1='torus'
                                    )

                        with self.uiCreateFrame('uiLAY_frameIconTextScrollLists', 'Icon Text Scroll Lists (PMIconTextScrollList)') as self.uiLAY_frameIconTextScrollLists:
                            with pm.columnLayout():
                                with pm.rowLayout(numberOfColumns=3):
                                    pm.separator(style='none', width=140)
                                    self.uiITSLST_test1 = pm.iconTextScrollList(
                                        'uiITSLST_test1',
                                        allowMultiSelection=True,
                                        append=('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
                                    )
                                    self.uiITSLST_test2 = pm.iconTextScrollList(
                                        'uiITSLST_test2',
                                        allowMultiSelection=True,
                                        append=('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
                                    )

                        with self.uiCreateFrame('uiLAY_frameIntFields', 'Int Fields (PMIntField)') as self.uiLAY_frameIntFields:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                with pm.rowLayout(numberOfColumns=3):
                                    pm.separator(width=140, style='none')
                                    self.uiINF_test1 = pm.floatField('uiINF_test1')
                                    self.uiINF_test2 = pm.floatField('uiINF_test2')

                        with self.uiCreateFrame('uiLAY_frameIntFieldGroups', 'Int Field Groups (PMIntFieldGrp#)') as self.uiLAY_frameIntFieldGroups:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                self.uiINFGRP_test1 = pm.intFieldGrp(
                                    'uiINFGRP_test1',
                                    numberOfFields=1,
                                    label='PMIntFieldGrp1'
                                )
                                self.uiINFGRP_test2 = pm.intFieldGrp(
                                    'uiINFGRP_test2',
                                    numberOfFields=2,
                                    label='PMIntFieldGrp2'
                                )
                                self.uiINFGRP_test3 = pm.intFieldGrp(
                                    'uiINFGRP_test3',
                                    numberOfFields=3,
                                    label='PMIntFieldGrp3'
                                )
                                self.uiINFGRP_test4 = pm.intFieldGrp(
                                    'uiINFGRP_test4',
                                    numberOfFields=4,
                                    label='PMIntFieldGrp4'
                                )

                        with self.uiCreateFrame('uiLAY_frameIntScrollBars', 'Int Scroll Bars (PMIntScrollBar)') as self.uiLAY_frameIntScrollBars:
                            with pm.columnLayout(adjustableColumn=True):
                                pm.separator(style='none', height=2)
                                self.uiINSCRL_test1 = pm.intScrollBar('uiINSCRL_test1')
                                self.uiINSCRL_test2 = pm.intScrollBar('uiINSCRL_test2')

                        with self.uiCreateFrame('uiLAY_frameIntSliders', 'Int Sliders (PMIntSlider)') as self.uiLAY_frameIntSliders:
                            with pm.columnLayout(adjustableColumn=True):
                                pm.separator(style='none', height=2)
                                self.uiINTSLD_test1 = pm.intSlider('uiINTSLD_test1')
                                self.uiINTSLD_test2 = pm.intSlider('uiINTSLD_test2')

                        with self.uiCreateFrame('uiLAY_frameIntSliderGroups', 'Int Slider Groups (PMIntSliderGrp)') as self.uiLAY_frameIntSliderGroups:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                self.uiINSGRP_test1 = pm.intSliderGrp(
                                    'uiINSGRP_test1',
                                    label='test1',
                                    field=True
                                )
                                self.uiINSGRP_test2 = pm.intSliderGrp(
                                    'uiINSGRP_test2',
                                    label='test2',
                                    field=True
                                )

                        with self.uiCreateFrame('uiLAY_frameOptionMenus', 'Option Menus (PMOptionMenu)') as self.uiLAY_frameOptionMenus:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                with pm.rowLayout(numberOfColumns=3):
                                    pm.separator(width=110, style='none')
                                    self.uiOPTMNU_test1 = pm.optionMenu('uiOPTMNU_test1', label='test1')
                                    pm.menuItem(label='one')
                                    pm.menuItem(label='two')
                                    pm.menuItem(label='three')
                                    self.uiOPTMNU_test2 = pm.optionMenu('uiOPTMNU_test2', label='test2')
                                    pm.menuItem(label='four')
                                    pm.menuItem(label='five')
                                    pm.menuItem(label='six')

                        with self.uiCreateFrame('uiLAY_frameOptionMenuGroups', 'Option Menus Groups (PMOptionMenuGrp)') as self.uiLAY_frameOptionMenuGroups:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                self.uiOPMGRP_test1 = pm.optionMenuGrp('uiOPMGRP_test1', label='test1', extraLabel='extraLabel')
                                pm.menuItem(label='one')
                                pm.menuItem(label='two')
                                pm.menuItem(label='three')
                                self.uiOPMGRP_test2 = pm.optionMenuGrp('uiOPMGRP_test2', label='test2', extraLabel='extraLabel')
                                pm.menuItem(label='four')
                                pm.menuItem(label='five')
                                pm.menuItem(label='six')

                        with self.uiCreateFrame('uiLAY_frameRadioButtons', 'Radio Buttons (PMRadioButton)') as self.uiLAY_frameRadioButtons:
                            with pm.columnLayout():
                                with pm.rowLayout(numberOfColumns=4):
                                    pm.separator(style='none', width=140)
                                    pm.radioCollection()
                                    self.uiRAD_test1 = pm.radioButton('uiRAD_test1', label='test1')
                                    self.uiRAD_test2 = pm.radioButton('uiRAD_test2', label='test2')
                                    self.uiRAD_test3 = pm.radioButton('uiRAD_test3', label='test3')

                        with self.uiCreateFrame('uiLAY_frameSymbolCheckBoxes', 'Symbol Check Boxes (PMSymbolCheckBox)') as self.uiLAY_frameSymbolCheckBoxes:
                            with pm.columnLayout():
                                with pm.rowLayout(numberOfColumns=3):
                                    pm.separator(style='none', width=140)
                                    self.uiSYMCHK_test1 = pm.symbolCheckBox(
                                        'uiSYMCHK_test1',
                                        image='polyCube'
                                    )
                                    self.uiSYMCHK_test2 = pm.symbolCheckBox(
                                        'uiSYMCHK_test2',
                                        image='polyCone'
                                    )

                        with self.uiCreateFrame('uiLAY_frameScriptTables', 'Script Tables (PMScriptTable)') as self.uiLAY_frameScriptTables:
                            with pm.columnLayout():
                                with pm.rowLayout(numberOfColumns=3):
                                    pm.separator(style='none', width=140)
                                    self.uiSCRTBL_test1 = pm.scriptTable(
                                        'uiSCRTBL_test1',
                                        selectionMode=3,
                                        rows=4,
                                        columns=2
                                    )
                                    self.uiSCRTBL_test2 = pm.scriptTable(
                                        'uiSCRTBL_test2',
                                        selectionMode=3,
                                        rows=4,
                                        columns=2
                                    )

                        with self.uiCreateFrame('uiLAY_frameScrollField', 'Scroll Field (PMScrollField)') as self.uiLAY_frameScrollField:
                            with pm.columnLayout():
                                with pm.rowLayout(numberOfColumns=3):
                                    pm.separator(style='none', width=140)
                                    self.uiSCRFLD_test1 = pm.scrollField(
                                        'uiSCRFLD_test1',
                                        wordWrap=True
                                    )
                                    self.uiSCRFLD_test2 = pm.scrollField(
                                        'uiSCRFLD_test2',
                                        wordWrap=True
                                    )

                        with self.uiCreateFrame('uiLAY_frameShelfTabLayout', 'Shelf Tab Layout (PMShelfTabLayout)') as self.uiLAY_frameShelfTabLayout:
                            with pm.columnLayout(adjustableColumn=True):
                                with pm.shelfTabLayout() as self.uiSHLTAB_test1:
                                    with pm.shelfLayout('test1'):
                                        pass
                                    with pm.shelfLayout('test2'):
                                        pass
                                    with pm.shelfLayout('test3'):
                                        pass
                                with pm.shelfTabLayout() as self.uiSHLTAB_test2:
                                    with pm.shelfLayout('test4'):
                                        pass
                                    with pm.shelfLayout('test5'):
                                        pass
                                    with pm.shelfLayout('test6'):
                                        pass

                        with self.uiCreateFrame('uiLAY_frameTabLayout', 'Tab Layout (PMTabLayout)') as self.uiLAY_frameTabLayout:
                            with pm.columnLayout(adjustableColumn=True):
                                with pm.tabLayout() as self.uiTAB_test1:

                                    with pm.rowLayout(numberOfColumns=1) as uiLAY_tabRow1:
                                        pass
                                    with pm.rowLayout(numberOfColumns=1) as uiLAY_tabRow2:
                                        pass
                                    with pm.rowLayout(numberOfColumns=1) as uiLAY_tabRow3:
                                        pass

                                pm.tabLayout(
                                    self.uiTAB_test1,
                                    edit=True,
                                    tabLabel=((uiLAY_tabRow1, 'test1'), (uiLAY_tabRow2, 'test2'), (uiLAY_tabRow3, 'test3'),)
                                )

                                with pm.tabLayout() as self.uiTAB_test2:

                                    with pm.rowLayout(numberOfColumns=1) as uiLAY_tabRow4:
                                        pass
                                    with pm.rowLayout(numberOfColumns=1) as uiLAY_tabRow5:
                                        pass
                                    with pm.rowLayout(numberOfColumns=1) as uiLAY_tabRow6:
                                        pass

                                pm.tabLayout(
                                    self.uiTAB_test2,
                                    edit=True,
                                    tabLabel=((uiLAY_tabRow4, 'test4'), (uiLAY_tabRow5, 'test5'), (uiLAY_tabRow6, 'test6'),)
                                )

                        with self.uiCreateFrame('uiLAY_frameTextFields', 'Text Fields (PMTextField)') as self.uiLAY_frameTextFields:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                with pm.rowLayout(numberOfColumns=3):
                                    pm.separator(width=140, style='none')
                                    self.uiTXT_test1 = pm.textField('uiTXT_test1')
                                    self.uiTXT_test2 = pm.textField('uiTXT_test2')

                        with self.uiCreateFrame('uiLAY_frameTextFieldButtonGroups', 'Text Field Button Groups (PMTextFieldButtonGrp)') as self.uiLAY_frameTextFieldButtonGroups:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                self.uiTXBTGR_test1 = pm.textFieldButtonGrp(
                                    'uiTXBTGR_test1',
                                    label='test1',
                                    buttonLabel='button1'
                                )
                                self.uiTXBTGR_test2 = pm.textFieldButtonGrp(
                                    'uiTXBTGR_test2',
                                    label='test2',
                                    buttonLabel='button2'
                                )

                        with self.uiCreateFrame('uiLAY_frameTextFieldGroups', 'Text Field Groups (PMTextFieldGrp)') as self.uiLAY_frameTextFieldGroups:
                            with pm.columnLayout():
                                pm.separator(style='none', height=2)
                                self.uiTXTGRP_test1 = pm.textFieldGrp(
                                    'uiTXTGRP_test1',
                                    label='test1'
                                )
                                self.uiTXTGRP_test2 = pm.textFieldGrp(
                                    'uiTXTGRP_test2',
                                    label='test2'
                                )

                        with self.uiCreateFrame('uiLAY_frameTextScrollLists', 'Text Scroll Lists (PMTextScrollList)') as self.uiLAY_frameTextScrollLists:
                            with pm.columnLayout():
                                with pm.rowLayout(numberOfColumns=3):
                                    pm.separator(style='none', width=140)
                                    self.uiTXTLST_test1 = pm.textScrollList(
                                        'uiTXTLST_test1',
                                        allowMultiSelection=True,
                                        append=('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
                                    )
                                    self.uiTXTLST_test2 = pm.textScrollList(
                                        'uiTXTLST_test2',
                                        allowMultiSelection=True,
                                        append=('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
                                    )

                self.uiBTN_savePrefs = pm.button(
                    label='Save Prefs',
                    height=MAIN_BUTTONS_HEIGHT,
                    command=self.onSavePrefsClicked
                )

                self.uiBTN_loadPrefs = pm.button(
                    label='Load Prefs',
                    height=MAIN_BUTTONS_HEIGHT,
                    command=self.onLoadPrefsClicked
                )

                self.uiBTN_resetPrefs = pm.button(
                    label='Reset Prefs',
                    height=MAIN_BUTTONS_HEIGHT,
                    command=self.onResetPrefsClicked
                )

                uiLAY_mainForm.attachForm(self.uiLAY_mainScroll, 'top', 2)
                uiLAY_mainForm.attachForm(self.uiLAY_mainScroll, 'left', 2)
                uiLAY_mainForm.attachForm(self.uiLAY_mainScroll, 'right', 2)
                uiLAY_mainForm.attachControl(self.uiLAY_mainScroll, 'bottom', 2, self.uiBTN_savePrefs)

                uiLAY_mainForm.attachNone(self.uiBTN_savePrefs, 'top')
                uiLAY_mainForm.attachForm(self.uiBTN_savePrefs, 'left', 2)
                uiLAY_mainForm.attachPosition(self.uiBTN_savePrefs, 'right', 2, 33)
                uiLAY_mainForm.attachForm(self.uiBTN_savePrefs, 'bottom', 2)

                uiLAY_mainForm.attachNone(self.uiBTN_loadPrefs, 'top')
                uiLAY_mainForm.attachPosition(self.uiBTN_loadPrefs, 'left', 2, 33)
                uiLAY_mainForm.attachPosition(self.uiBTN_loadPrefs, 'right', 2, 66)
                uiLAY_mainForm.attachForm(self.uiBTN_loadPrefs, 'bottom', 2)

                uiLAY_mainForm.attachNone(self.uiBTN_resetPrefs, 'top')
                uiLAY_mainForm.attachPosition(self.uiBTN_resetPrefs, 'left', 2, 66)
                uiLAY_mainForm.attachForm(self.uiBTN_resetPrefs, 'right', 2)
                uiLAY_mainForm.attachForm(self.uiBTN_resetPrefs, 'bottom', 2)

        self.window.setTitle(self.window.__class__)

    # noinspection PyMethodMayBeStatic
    def uiCreateFrame(self, controlName, name, collapsed=False):
        return pm.frameLayout(
            controlName,
            label=name,
            collapsable=True,
            marginHeight=3,
            borderStyle='etchedIn',
            borderVisible=True,
            collapse=collapsed
        )

    # noinspection PyMethodMayBeStatic
    def createSerializer(self, ser):
        if ser == 'SerializerFilePickle':
            from fxpt.fx_prefsaver.SerializerFilePickle import SerializerFilePickle
            return SerializerFilePickle(CFG_FILENAME)
        if ser == 'SerializerFileJson':
            from fxpt.fx_prefsaver.SerializerFileJson import SerializerFileJson
            return SerializerFileJson(CFG_FILENAME)
        elif ser == 'SerializerOptVars':
            from fxpt.fx_prefsaver.SerializerOptVars import SerializerOptVars
            return SerializerOptVars('TestQtWindow')
        else:
            assert False, 'Unknown serializer type'

    def initPrefs(self):
        self.prefSaver.addControl(self.uiCHK_test1, PrefSaver.UIType.PMCheckBox, False)
        self.prefSaver.addControl(self.uiCHK_test2, PrefSaver.UIType.PMCheckBox, False)

    # noinspection PyUnusedLocal
    def onSavePrefsClicked(self, *args):
        self.prefSaver.savePrefs()

    # noinspection PyUnusedLocal
    def onLoadPrefsClicked(self, *args):
        self.prefSaver.loadPrefs()

    # noinspection PyUnusedLocal
    def onResetPrefsClicked(self, *args):
        self.prefSaver.resetPrefs()

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def onCloseClicked(self, *args):
        if pm.window(WIN_NAME, exists=True):
            pm.deleteUI(WIN_NAME, window=True)



def run(serializer):
    WinPyMelUI(serializer)