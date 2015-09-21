#!/usr/bin/env python3

import sys
import json
import sqlite3


def main():
    with open('./fcq.clean.json', 'r') as f:
        data = json.loads(f.read())
    conn = sqlite3.connect('fcq.db')
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS fcq')
    c.execute('DROP TABLE IF EXISTS n')
    c.execute('DROP TABLE IF EXISTS pct')
    c.execute('DROP TABLE IF EXISTS workload')

    c.execute(('CREATE TABLE fcq('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'AVG_GRD REAL, '
                'Activity_Type TEXT, '
                'AvgCourse REAL, '
                'AvgInstructor REAL, '
                'Course INTEGER, '
                'CourseTitle TEXT, '
                'CrsLvlNum TEXT, '
                'CrsPBAColl TEXT, '
                'CrsPBADept TEXT, '
                'CrsPBADiv TEXT, '
                'Honors INTEGER, '
                'Hours INTEGER, '
                'Instruction_Mode TEXT, '
                'Level TEXT, '
                'NComb INTEGER, '
                'NIntrFCQ INTEGER, '
                'N INTEGER, '
                'PCT INTEGER, '
                'RAP INTEGER, '
                'Section INTEGER, '
                'Subject TEXT, '
                'Subject_Label TEXT, '
                'Workload INTEGER, '
                'YearTerm INTEGER, '
                'Instructors TEXT, '
                'FOREIGN KEY(N) REFERENCES n(id), '
                'FOREIGN KEY(PCT) REFERENCES pct(id), '
                'FOREIGN KEY(Workload) REFERENCES workload(id))'))

    c.execute(('CREATE TABLE n('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'ENROLL INTEGER, '
                'EOT INTEGER, '
                'GRADE INTEGER, '
                'INCOMP INTEGER, '
                'NOCRED INTEGER, '
                'PASS INTEGER, '
                'Ret INTEGER)'))
    c.execute(('CREATE TABLE pct('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'A REAL, '
                'B REAL, '
                'C REAL, '
                'C_MINUS_OR_BELOW REAL, '
                'D REAL, '
                'DF REAL, '
                'F REAL, '
                'GRADE INTEGER, '
                'INCOMP REAL, '
                'WDRAW REAL)'))
    c.execute(('CREATE TABLE workload('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'Hrs_Wk TEXT, '
                'Raw REAL)'))

    nid    = 1
    pctid  = 1
    workid = 1
    for fcq in data:
        c.execute(('INSERT INTO n(ENROLL, EOT, GRADE, INCOMP, NOCRED, PASS, Ret) '
                    'VALUES (?, ?, ?, ?, ?, ?, ?)'),
                    (fcq['N']['ENROLL'],
                     fcq['N']['EOT'],
                     fcq['N']['GRADE'],
                     fcq['N']['INCOMP'],
                     fcq['N']['NOCRED'],
                     fcq['N']['PASS'],
                     fcq['N']['Ret']))
        c.execute(('INSERT INTO pct(A, B, C, C_MINUS_OR_BELOW, D, DF, F, GRADE, INCOMP, WDRAW) '
                    'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'),
                    (fcq['PCT']['A'],
                     fcq['PCT']['B'],
                     fcq['PCT']['C'],
                     fcq['PCT']['C_MINUS_OR_BELOW'],
                     fcq['PCT']['D'],
                     fcq['PCT']['DF'],
                     fcq['PCT']['F'],
                     fcq['PCT']['GRADE'],
                     fcq['PCT']['INCOMP'],
                     fcq['PCT']['WDRAW']))
        c.execute(('INSERT INTO workload(Hrs_Wk, Raw) '
                    'VALUES (?, ?)'),
                    (fcq['Workload']['Hrs_Wk'],
                     fcq['Workload']['Raw']))
        keys = ['AVG_GRD','Activity_Type','AvgCourse','AvgInstructor',
                'Course','CourseTitle','CrsLvlNum','CrsPBAColl','CrsPBADept',
                'CrsPBADiv','Honors','Hours','Instruction_Mode','Level',
                'NComb','NIntrFCQ','N','PCT','RAP','Section',
                'Subject','Subject_Label','Workload','YearTerm','Instructor']

        values = []
        nkeys = []
        for k in keys:
            if k == 'N':
                values.append(nid)
                nkeys.append(k)
            elif k == 'PCT':
                values.append(pctid)
                nkeys.append(k)
            elif k == 'Workload':
                values.append(workid)
                nkeys.append(k)
            else:
                try:
                    values.append(fcq[k])
                    nkeys.append(k)
                except KeyError:
                    print('missing', k)
                    pass
        columns = ','.join(nkeys)
        question_marks = ','.join(['?'] * len(nkeys))

        query = 'INSERT INTO fcq({}) VALUES ({})'.format(columns, question_marks)

        c.execute(query, tuple(values))

        nid += 1
        pctid += 1
        workid += 1


    conn.commit()

if __name__ == '__main__':
    sys.exit(main())
