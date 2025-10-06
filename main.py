
"""Module de manipulation de mots français à partir d'un corpus."""


FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")

#### Fonctions secondaires

def read_data(filename):
    """Lit le fichier et retourne la liste des mots."""
    with open(filename, encoding="utf-8") as f:
        mots = [ligne.strip() for ligne in f]
    return mots


def ensemble_mots(filename):
    """Retourne l'ensemble des mots contenus dans filename."""
    return set(read_data(filename))


def mots_de_n_lettres(mots, n):
    """Retourne le sous-ensemble des mots de n lettres."""
    return {mot for mot in mots if len(mot) == n}


def mots_avec(mots, s):
    """Retourne le sous-ensemble des mots incluant la chaîne s."""
    return {mot for mot in mots if s in mot}


def cherche1(mots, start, stop, n):
    """Retourne les mots de n lettres commençant par start et finissant par stop."""
    res = mots_de_n_lettres(mots, n)
    if start:
        res = {mot for mot in res if mot.startswith(start)}
    if stop:
        res = {mot for mot in res if mot.endswith(stop)}
    return res


def cherche2(mots, lstart, lmid, lstop, nmin, nmax):    
    """Recherche complexe dans un ensemble de mots."""
    if isinstance(lstart, str):
        lstart = [lstart]
    if isinstance(lmid, str):
        lmid = [lmid]
    if isinstance(lstop, str):
        lstop = [lstop]
    res = set()
    for mot in mots:
        if nmin <= len(mot) <= nmax:
            if any(mot.startswith(prefix) for prefix in lstart):
                if any(med in mot for med in lmid):
                    if any(mot.endswith(suffix) for suffix in lstop):
                        res.add(mot)
    return res

def main():
    """Point d'entrée du programme."""
    return None



if __name__ == "__main__":
    main()

# def main():
#     mots = liste_mots(FILENAME)
    
#     print( [ mots[i] for i in [24499, 28281, 57305, 118091, 199316, 223435, 336455] ])
#     # ['bachi-bouzouks', 'bayadères', 'coloquintes', 'ectoplasmes', 'macchabées', 'oryctéropes', 'zouaves']
    
#     print([ mot for mot in ["chronophage", "procrastinateur", "dangerosité", "gratifiant"] if mot in mots ])
#     # ['dangerosité', 'gratifiant']
    
#     m7 = mots_de_n_lettres(mots, 7)
#     print(len(m7))
#     # # 27945 mots de 7 lettres
#     print( random.sample(list(m7), 5))

#     mk = mots_avec(mots, 'k')
#     print(len(mk))
#     # # 1621 mots contenant un k
#     print( random.sample(list(mk), 5))

#     m7k = m7 & mk
#     print(len(m7k))
#     # 180 mots de 7 lettres contenant un k

#     mw = mots_avec(mots, 'w')
#     mkw = mk & mw
#     print(len(mkw))
#     # 32 mots contenant un k ET un w

#     mz = mots_avec(mots, 'z')
#     print(len(mz))
#     # 35177 mots contenant un z

#     m_z = { mot for mot in mz if mot.startswith('z')}
#     print(len(m_z))    
#     # 796 mots commençant par z

#     mz_ = { mot for mot in mz if mot.endswith('z')}
#     print(len(mz_))    
#     # 33118 mots terminant par z

#     mznt = mz - m_z - mz_
#     print(len(mznt))
#     # print()
#     # # 1330 mots avec z en position non terminale

#     print(m_z & mz_)

#     print(mznt&mk)

#     m_k = { mot for mot in mk if mot.startswith('k')}
#     print(len(m_k))    
#     # 491 mots commençant par k

#     mk_ = { mot for mot in mk if mot.endswith('k')}
#     print(len(mk_))    
#     # 84 mots terminant par k

#     mknt = mk - m_k - mk_
#     print(len(mknt))
#     # print()
#     # 1052 mots avec k en position non terminale

#     print(mknt&mz)


# if __name__ == "__main__":
#     main()