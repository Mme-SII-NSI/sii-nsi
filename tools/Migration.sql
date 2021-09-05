-- desactivation des foreign key
PRAGMA foreign_keys=off;

-- competences_activite
ALTER TABLE "competences_activite"
RENAME TO "competences_activite_old";

CREATE TABLE "competences_activite" (
    "id"        integer         NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "titre"     varchar(200)    NOT NULL, 
    "code"      varchar(20)     NOT NULL, 
    "type"      varchar(50)     NOT NULL, 
    "lien_pdf"  varchar(200)    NULL,
    "programme_id"  integer     NOT NULL REFERENCES "competences_programme" ("id") DEFERRABLE INITIALLY DEFERRED
);



-- competences_programme
ALTER TABLE "competences_matiere"
RENAME TO "competences_matiere_old";

CREATE TABLE "competences_programme" (
    "id"    integer     NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "titre" varchar(20) NOT NULL
);

INSERT INTO "competences_programme" ("id", "titre")
VALUES 
    (1, 'SII 2015-2020'),
    (2, 'SII 2021-....');

DROP TABLE "competences_matiere_old";

-- competences_classe
ALTER TABLE "competences_classe"
RENAME TO "competences_classe_old";

CREATE TABLE "competences_classe" (
    "id"            integer     NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "classe"        varchar(50) NOT NULL    
);

INSERT INTO "competences_classe" ("id", "classe")
SELECT id, niveau
FROM competences_classe_old
WHERE id_matiere_id <> 2;


-- competences_etudiant
ALTER TABLE "competences_utilisateur"
RENAME TO "competences_utilisateur_old";

CREATE TABLE "competences_etudiant" (
    "id"            integer         NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "nom"           varchar(100)    NOT NULL, 
    "prenom"        varchar(100)    NOT NULL, 
    "auth_user_id"  integer         NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);

INSERT INTO "competences_etudiant" ("id", "nom", "prenom", "auth_user_id")
SELECT id, nom, prenom, username_id
FROM competences_utilisateur_old
WHERE id <> 85;

DROP TABLE "competences_utilisateur_old";

-- competences_promotion
-- competences_etudiant_promotion
ALTER TABLE "competences_promotion"
RENAME TO "competences_promotion_old";

CREATE TABLE "competences_promotion" (
    "id"            integer     NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "annee"         varchar(20) NOT NULL, 
    "classe_id"     integer     NOT NULL REFERENCES "competences_classe" ("id") DEFERRABLE INITIALLY DEFERRED,
    "programme_id"  integer     NOT NULL REFERENCES "competences_programme" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE "competences_etudiant_promotion" (
    "id"            integer     NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "promotion_id"  integer     NOT NULL REFERENCES "competences_promotion" ("id") DEFERRABLE INITIALLY DEFERRED, 
    "etudiant_id"      integer     NOT NULL REFERENCES "competences_etudiant" ("id") DEFERRABLE INITIALLY DEFERRED
);

INSERT INTO "competences_promotion" ("annee", "classe_id", "programme_id")
SELECT annee, id_classe_id, id_matiere_id
FROM competences_promotion_old
JOIN competences_classe_old ON id_classe_id = competences_classe_old.id
GROUP BY annee, id_classe_id;

INSERT INTO "competences_etudiant_promotion" ("promotion_id", "etudiant_id")
SELECT PROM.id, OLD.id_utilisateurP_id
FROM competences_promotion_old AS OLD
JOIN competences_promotion AS PROM ON PROM.annee = OLD.annee AND PROM.classe_id = OLD.id_classe_id;

DROP TABLE "competences_promotion_old";
DROP TABLE "competences_classe_old";

-- competences_bilan
ALTER TABLE "competences_bilan"
RENAME TO "competences_bilan_old";

-- CREATE TABLE "competences_bilan" (
--     "id"                integer         NOT NULL PRIMARY KEY AUTOINCREMENT, 
--     "date"              datetime        NOT NULL, 
--     "libelle"           varchar(100)    NOT NULL, 
--     "utilisateur_id"    integer         NOT NULL REFERENCES "competences_utilisateur" ("id") DEFERRABLE INITIALLY DEFERRED
-- );

DROP TABLE "competences_bilan_old";

-- competences_competence
ALTER TABLE "competences_competence"
RENAME TO "competences_competence_old";

CREATE TABLE "competences_competence" (
    "id"                integer         NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "competence"        varchar(200)    NOT NULL, 
    "code"              varchar(50)     NOT NULL, 
    "sous_competence"   varchar(200)    NOT NULL, 
    "image"             varchar(100)    NOT NULL, 
    "programme_id"      integer NOT NULL REFERENCES "competences_programme" ("id") DEFERRABLE INITIALLY DEFERRED
);

INSERT INTO "competences_competence" ("id", "competence", "code", "sous_competence", "image", "programme_id")
SELECT id, competence_text, code_competence, souscompetence_text, image_mini, id_matiere_id
FROM competences_competence_old
WHERE id_matiere_id <> 2;

DROP TABLE "competences_competence_old";

-- competences_theme
ALTER TABLE "competences_theme"
RENAME TO "competences_theme_old";

CREATE TABLE "competences_theme" (
    "id"            integer     NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "theme"         varchar(50) NOT NULL, 
    "programme_id"  integer     NOT NULL REFERENCES "competences_programme" ("id") DEFERRABLE INITIALLY DEFERRED
);

INSERT INTO "competences_theme" ("id", "theme", "programme_id")
SELECT id, theme_textP, id_matiere_id
FROM competences_theme_old
WHERE id_matiere_id <> 2;

DROP TABLE "competences_theme_old";

-- competences_detail_competence
CREATE TABLE "competences_detail_competence" (
    "id"            integer         NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "titre"         varchar(200)    NOT NULL, 
    "code"          varchar(50)     NOT NULL, 
    "competence_id" integer         NOT NULL REFERENCES "competences_competence" ("id") DEFERRABLE INITIALLY DEFERRED,
    "theme_id"      integer         NOT NULL REFERENCES "competences_theme" ("id") DEFERRABLE INITIALLY DEFERRED,
    "programme_id"  integer         NOT NULL REFERENCES "competences_programme" ("id") DEFERRABLE INITIALLY DEFERRED
);

-- competences_ligne_bilan
ALTER TABLE "competences_lignebilan"
RENAME TO "competences_lignebilan_old";

-- CREATE TABLE "competences_ligne_bilan" (
--     "id"                    integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
--     "est_acquis"            integer NOT NULL, 
--     "modulation"            integer NOT NULL, 
--     "bilan_id"              integer NOT NULL REFERENCES "competences_bilan" ("id") DEFERRABLE INITIALLY DEFERRED, 
--     "detail_competence_id"  integer NOT NULL REFERENCES "competences_detail_competence" ("id") DEFERRABLE INITIALLY DEFERRED
-- );

DROP TABLE "competences_lignebilan_old";

-- competences_question
ALTER TABLE "competences_question"
RENAME TO "competences_question_old";

CREATE TABLE "competences_question" (
    "id"                    integer         NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "num_question"          varchar(8)      NOT NULL, 
    "point"                 integer         NOT NULL,
    "activite_id"           integer         NOT NULL REFERENCES "competences_activite" ("id") DEFERRABLE INITIALLY DEFERRED, 
    "detail_competence_id"  integer         NOT NULL REFERENCES "competences_detail_competence" ("id") DEFERRABLE INITIALLY DEFERRED
);

-- competences_note_etudiant
ALTER TABLE "competences_noteutilisateur"
RENAME TO "competences_noteutilisateur_old";

CREATE TABLE "competences_note_etudiant" (
    "id"                integer     NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "note"              integer     NOT NULL, 
    "acquis"            integer     NOT NULL,
    "date"              datetime    NOT NULL, 
    "question_id"       integer     NOT NULL REFERENCES "competences_question" ("id") DEFERRABLE INITIALLY DEFERRED, 
    "etudiant_id"       integer     NOT NULL REFERENCES "competences_etudiant" ("id") DEFERRABLE INITIALLY DEFERRED
);

INSERT INTO "competences_note_etudiant" ("id", "note", "acquis", "date", "question_id", "etudiant_id")
SELECT id, note, note, date_note, id_question_id, id_utilisateurN_id
FROM competences_noteutilisateur_old
WHERE id_utilisateurN_id <> 85;

DROP TABLE "competences_noteutilisateur_old";


-- migration des details_competence
INSERT INTO "competences_detail_competence" ("titre", "code", "competence_id", "theme_id", "programme_id")
SELECT DISTINCT
	quest.intitule_textQ AS titre,
	quest.intitule_textQ AS code,
	quest.code_competenceQ_id AS competenceId,
	quest.themeQ_id AS themeId,
    comp.programme_id
FROM
competences_question_old AS quest
INNER JOIN competences_competence AS comp on comp.id = quest.code_competenceQ_id
INNER JOIN competences_theme AS theme on theme.id = quest.themeQ_id
WHERE comp.programme_id <> 2;

INSERT INTO "competences_activite" ("id", "titre", "code", "type", "lien_pdf", "programme_id")
SELECT 
	id, 
	titre_text, 
	code_act, 
	type, lien_pdf, 
	(SELECT programme_id 
	 FROM competences_question_old AS quest
	 INNER JOIN competences_detail_competence AS detail ON detail.titre = quest.intitule_textQ and detail.theme_id = quest.themeQ_id and detail.competence_id = quest.code_competenceQ_id) as t
FROM competences_activite_old;

INSERT INTO "competences_question" ("id", "num_question", "point", "activite_id", "detail_competence_id")
SELECT quest.id, quest.num_question, quest.point, quest.code_actQ_id, detail.id
FROM competences_question_old AS quest
INNER JOIN competences_detail_competence AS detail ON detail.titre = quest.intitule_textQ and detail.theme_id = quest.themeQ_id and detail.competence_id = quest.code_competenceQ_id;

DROP TABLE "competences_question_old";
DROP TABLE "competences_activite_old";



-- activation des foreign key
PRAGMA foreign_keys=on;


-- Suppression des doublons
DELETE FROM competences_note_etudiant
WHERE id in (
SELECT id
FROM (
	SELECT
		COUNT(*) AS nb,
		MIN(id) AS id,
		question_id,
		etudiant_id
	FROM
	competences_note_etudiant
	GROUP BY 
		question_id,
		etudiant_id
) AS note
WHERE nb > 1);
DELETE FROM competences_note_etudiant
WHERE id in (
SELECT id
FROM (
	SELECT
		COUNT(*) AS nb,
		MIN(id) AS id,
		question_id,
		etudiant_id
	FROM
	competences_note_etudiant
	GROUP BY 
		question_id,
		etudiant_id
) AS note
WHERE nb > 1);
DELETE FROM competences_note_etudiant
WHERE id in (
SELECT id
FROM (
	SELECT
		COUNT(*) AS nb,
		MIN(id) AS id,
		question_id,
		etudiant_id
	FROM
	competences_note_etudiant
	GROUP BY 
		question_id,
		etudiant_id
) AS note
WHERE nb > 1);

