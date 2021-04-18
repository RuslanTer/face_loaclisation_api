-- upgrade --
ALTER TABLE "image" ADD "count_faces" INT NOT NULL;
-- downgrade --
ALTER TABLE "image" DROP COLUMN "count_faces";
