namespace PiSync.Room.Update
{
    partial class RoomUpdateForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            label3 = new Label();
            tbRoomStatus = new ComboBox();
            label2 = new Label();
            tbDoorStatus = new ComboBox();
            btnUpdate = new Button();
            label1 = new Label();
            tbRoomName = new TextBox();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = SystemColors.Window;
            panel1.Controls.Add(label3);
            panel1.Controls.Add(tbRoomStatus);
            panel1.Controls.Add(label2);
            panel1.Controls.Add(tbDoorStatus);
            panel1.Controls.Add(btnUpdate);
            panel1.Controls.Add(label1);
            panel1.Controls.Add(tbRoomName);
            panel1.Location = new Point(38, 30);
            panel1.Name = "panel1";
            panel1.Size = new Size(346, 354);
            panel1.TabIndex = 1;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Courier New", 11F);
            label3.Location = new Point(26, 197);
            label3.Name = "label3";
            label3.Size = new Size(131, 21);
            label3.TabIndex = 9;
            label3.Text = "ROOM STATUS";
            // 
            // tbRoomStatus
            // 
            tbRoomStatus.DropDownStyle = ComboBoxStyle.DropDownList;
            tbRoomStatus.FormattingEnabled = true;
            tbRoomStatus.Items.AddRange(new object[] { "ACTIVE", "INACTIVE" });
            tbRoomStatus.Location = new Point(26, 221);
            tbRoomStatus.Name = "tbRoomStatus";
            tbRoomStatus.Size = new Size(288, 30);
            tbRoomStatus.TabIndex = 8;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Courier New", 11F);
            label2.Location = new Point(26, 114);
            label2.Name = "label2";
            label2.Size = new Size(142, 21);
            label2.TabIndex = 7;
            label2.Text = "DOOR STATUS:";
            // 
            // tbDoorStatus
            // 
            tbDoorStatus.DropDownStyle = ComboBoxStyle.DropDownList;
            tbDoorStatus.FormattingEnabled = true;
            tbDoorStatus.Items.AddRange(new object[] { "OPEN", "CLOSE" });
            tbDoorStatus.Location = new Point(26, 138);
            tbDoorStatus.Name = "tbDoorStatus";
            tbDoorStatus.Size = new Size(288, 30);
            tbDoorStatus.TabIndex = 6;
            // 
            // btnUpdate
            // 
            btnUpdate.Cursor = Cursors.Hand;
            btnUpdate.Location = new Point(26, 293);
            btnUpdate.Name = "btnUpdate";
            btnUpdate.Size = new Size(289, 47);
            btnUpdate.TabIndex = 5;
            btnUpdate.Text = "UPDATE";
            btnUpdate.UseVisualStyleBackColor = true;
            btnUpdate.Click += btnUpdate_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Courier New", 11F);
            label1.Location = new Point(26, 37);
            label1.Name = "label1";
            label1.Size = new Size(120, 21);
            label1.TabIndex = 3;
            label1.Text = "Room Name:";
            // 
            // tbRoomName
            // 
            tbRoomName.Location = new Point(26, 64);
            tbRoomName.Name = "tbRoomName";
            tbRoomName.PlaceholderText = "Enter room name";
            tbRoomName.Size = new Size(289, 30);
            tbRoomName.TabIndex = 2;
            // 
            // RoomUpdateForm
            // 
            AutoScaleDimensions = new SizeF(12F, 22F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(426, 421);
            Controls.Add(panel1);
            Font = new Font("Courier New", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.FixedToolWindow;
            Margin = new Padding(4, 3, 4, 3);
            Name = "RoomUpdateForm";
            StartPosition = FormStartPosition.CenterParent;
            Text = "UPDATE ROOM";
            Load += RoomUpdateForm_Load;
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Button btnUpdate;
        private Label label1;
        private TextBox tbRoomName;
        private Label label3;
        private ComboBox tbRoomStatus;
        private Label label2;
        private ComboBox tbDoorStatus;
    }
}