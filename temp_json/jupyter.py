{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Credit</th>\n",
       "      <th>EGP</th>\n",
       "      <th>SGPA</th>\n",
       "      <th>Unnamed: 4</th>\n",
       "      <th>Unnamed: 5</th>\n",
       "      <th>Credit.1</th>\n",
       "      <th>EGP.1</th>\n",
       "      <th>CGPA</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>SGPA</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>CGPA</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>21</td>\n",
       "      <td>120</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.71</td>\n",
       "      <td>NaN</td>\n",
       "      <td>21</td>\n",
       "      <td>120.0</td>\n",
       "      <td>5.71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>DE 0</td>\n",
       "      <td>DC 0 HM</td>\n",
       "      <td>3 OC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00</td>\n",
       "      <td>DE 0</td>\n",
       "      <td>DC 0 HM</td>\n",
       "      <td>3.0</td>\n",
       "      <td>OC 0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AU 0</td>\n",
       "      <td>ES 9 BS</td>\n",
       "      <td>9 Total</td>\n",
       "      <td>NaN</td>\n",
       "      <td>21.00</td>\n",
       "      <td>AU 0</td>\n",
       "      <td>ES 9 BS</td>\n",
       "      <td>9.0</td>\n",
       "      <td>Total 21</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Unnamed: 0   Credit      EGP  SGPA  Unnamed: 4 Unnamed: 5 Credit.1  EGP.1  \\\n",
       "0       SGPA      NaN      NaN   NaN         NaN       CGPA      NaN    NaN   \n",
       "1        NaN       21      120   NaN        5.71        NaN       21  120.0   \n",
       "2       DE 0  DC 0 HM     3 OC   NaN        0.00       DE 0  DC 0 HM    3.0   \n",
       "3       AU 0  ES 9 BS  9 Total   NaN       21.00       AU 0  ES 9 BS    9.0   \n",
       "\n",
       "       CGPA  \n",
       "0       NaN  \n",
       "1      5.71  \n",
       "2      OC 0  \n",
       "3  Total 21  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from tabula import read_pdf\n",
    "import json\n",
    "read_pdf(\"cse.pdf\",area=[])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[383.00001249999997, 9.00011875, 428.3687625, 286.41886875]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p=[]\n",
    "p.append(obj[0][\"y1\"])\n",
    "p.append(obj[0][\"x1\"])\n",
    "p.append(obj[0][\"y2\"])\n",
    "p.append(obj[0][\"x2\"])\n",
    "p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 248,
   "metadata": {},
   "outputs": [],
   "source": [
    "del str"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[383.00001249999997, 9.00011875, 428.3687625, 286.41886875],\n",
       " [169.946875, 7.809375, 260.684375, 286.715625],\n",
       " [171.43437500000002, 302.334375, 262.91562500000003, 578.265625],\n",
       " [323.903125, 10.040625, 381.91562500000003, 285.22812500000003],\n",
       " [264.403125, 302.334375, 307.54062500000003, 581.984375],\n",
       " [263.659375, 10.040625, 308.284375, 288.94687500000003],\n",
       " [102.265625, 8.553125, 132.759375, 579.7531250000001]]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "with open('cse226.template_777.json', 'r') as fp:\n",
    "    obj = json.load(fp)\n",
    "a=[]\n",
    "for i in range(len(obj)):\n",
    "    p=[]\n",
    "    p.append(obj[i][\"y1\"])\n",
    "    p.append(obj[i][\"x1\"])\n",
    "    p.append(obj[i][\"y2\"])\n",
    "    p.append(obj[i][\"x2\"])\n",
    "    a.append(p)\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[169.946875, 7.809375, 260.684375, 286.715625]"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p=[]\n",
    "p.append(obj[1][\"y1\"])\n",
    "p.append(obj[1][\"x1\"])\n",
    "p.append(obj[1][\"y2\"])\n",
    "p.append(obj[1][\"x2\"])\n",
    "p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0         DISCRETE MATHEMATICS AND GRAPH THEORY (DC)\n",
       "1         DATA STRUCTURE AND PROGRAM DESIGN - I (DC)\n",
       "2               INTRODUCTION TO WEB PROGRAMMING (DE)\n",
       "3           DIGITAL CIRCUITS AND MICROPROCESSOR (DC)\n",
       "4                              SOFTWARE LAB - I (DC)\n",
       "5    PROBABILITY THEORY AND STATISTICAL METHODS (DC)\n",
       "Name: 1, dtype: object"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = read_pdf('cse.pdf',pages=227,area=a[3],multiple_tables=True,guess=False)\n",
    "# df[0][0] code\n",
    "df[0][1] #course\n",
    "# df[0][2] credits\n",
    "# df[0][3] scored"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 251,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Code: MAL208\\nCourse: PROBABILITY THEORY AND STATISTICAL METHODS (DC)\\nCredits: 4\\nGradeBB'"
      ]
     },
     "execution_count": 251,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = read_pdf('cse.pdf', pages=227, area=a[3], guess=False,pandas_options={'names': ['Code', 'Course', 'Credits', 'Grade']})\n",
    "# df\n",
    "# global str\n",
    "for i in range(len(df)):\n",
    "    d = \"Code: \"+df['Code'][i]+\"\\n\"+\"Course: \" + df['Course'][i] +'\\n'+ \"Credits: \"+str(df['Credits'][i].item())+\"\\n\"+\"Grade: \"+df['Grade'][i]\n",
    "d\n",
    "\n",
    "# for i in range(len(df)):\n",
    "#     d = 'Code: '+df[0][0]+'\\n'+'Course: ' + df[0][1] +'\\n'+ 'Credits: '+df[0][2]+'\\n'+'Grade'+df[0][3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 195,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = read_pdf('cse.pdf',pages=227,area=a[3],guess=False,pandas_options={'names': ['Code','Course','Credits','Grade']})\n",
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24"
      ]
     },
     "execution_count": 187,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = read_pdf('cse.pdf',pages=227,area=a,multiple_tables=True,guess=False)\n",
    "str = df[0][3][3]\n",
    "c = int(str[5:])\n",
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 257,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24"
      ]
     },
     "execution_count": 257,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = read_pdf('cse.pdf',pages=227,area=a[0],multiple_tables=True,guess=False)\n",
    "cg = df[0][6][1]\n",
    "sg = df[0][3][1]\n",
    "cg\n",
    "sg\n",
    "c_cre = df[0][7][3]\n",
    "s_cre = df[0][3][3]\n",
    "s_cre = int(s_cre[5:])\n",
    "c_cre = int(c_cre[5:])\n",
    "c_cre\n",
    "s_cre\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'AAYUSH RAJESH JADHAV'"
      ]
     },
     "execution_count": 193,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = read_pdf('cse.pdf',pages=147,area=a,multiple_tables=True,guess=False)\n",
    "df[6][2][0]\n",
    "# df[6][2][1] branch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'BT17CSE082'"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = read_pdf('cse.pdf',pages=227,area=a,multiple_tables=True,guess=False)\n",
    "enroll=df[6][5][0]\n",
    "enroll"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Total67'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = read_pdf('cse.pdf', pages=182, area=a[0], guess=False,pandas_options={'header':None})\n",
    "df\n",
    "cg = df[6][1]\n",
    "sg = df[3][1]\n",
    "sg\n",
    "cg\n",
    "c_cre = df[7][3]\n",
    "s_cre = df[3][3]\n",
    "s_cre = s_cre[5:]\n",
    "c_cre = c_cre[5:]\n",
    "c_cre = df[7][3]\n",
    "s_cre = df[3][3]\n",
    "s_cre \n",
    "c_cre"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3rc1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
