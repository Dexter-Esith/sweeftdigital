CREATE TABLE [dbo].[Pupil](
[Id] [int] IDENTITY(1,1) NOT NULL,
[Firstname] [nvarchar](50) NOT NULL,
[Lastname] [nvarchar](50) NOT NULL,
[IsMale] [bit] NOT NULL,
[Class] [varchar](50) NOT NULL,
PRIMARY KEY (ID))

CREATE TABLE [dbo].[Teacher](
[Id] [int] IDENTITY(1,1) NOT NULL,
[Firstname] [nvarchar](50) NOT NULL,
[Lastname] [nvarchar](50) NOT NULL,
[IsMale] [bit] NOT NULL,
[Subject] [nvarchar](50) NOT NULL,
PRIMARY KEY (ID))


CREATE TABLE [dbo].[TeacherToPupil](
[Id] [int] IDENTITY(1,1) NOT NULL,
[TeacherId] [int] NOT NULL,
[PupilId] [int] NOT NULL,
 PRIMARY KEY (ID))

ALTER TABLE [dbo].[TeacherToPupil]  WITH CHECK ADD  CONSTRAINT [FK_TeacherToPupil_Pupil] FOREIGN KEY([PupilId])
REFERENCES [dbo].[Pupil] ([Id])

ALTER TABLE [dbo].[TeacherToPupil] CHECK CONSTRAINT [FK_TeacherToPupil_Pupil]

ALTER TABLE [dbo].[TeacherToPupil]  WITH CHECK ADD  CONSTRAINT [FK_TeacherToPupil_Teacher] FOREIGN KEY([TeacherId])
REFERENCES [dbo].[Teacher] ([Id])

ALTER TABLE [dbo].[TeacherToPupil] CHECK CONSTRAINT [FK_TeacherToPupil_Teacher]