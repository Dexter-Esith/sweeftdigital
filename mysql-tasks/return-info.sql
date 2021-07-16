SELECT Teacher.*
FROM Teacher
JOIN TeacherToPupil
 ON Teacher.Id = TeacherToPupil.TeacherId
JOIN Pupil
 ON Pupil.Id = TeacherToPupil.PupilId
 where Pupil.Firstname = N'გიორგი'